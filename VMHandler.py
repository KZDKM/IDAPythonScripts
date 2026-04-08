import ida_bytes
import ida_ua
import idaapi
import idc
from triton import *


def print_bytes(b):
    print(" ".join(f"{b:02x}" for b in b))


def vm_handler(cur_ea, ctx: TritonContext):
    rips = []  # record rip values
    disasm_inst = []  # save disassembled instructions

    code = BasicBlock()
    # somehow the first instruction in a new basicblock has wrong address
    code.add(
        Instruction(b"\x90")
    )  # hack fix, have no idea what the actual fuck is going on

    count = 0
    while count < 1000:
        disasm = idc.generate_disasm_line(cur_ea, 0)
        disasm = idaapi.tag_remove(disasm)
        insn = ida_ua.insn_t()
        length = ida_ua.decode_insn(insn, cur_ea)

        if insn.get_canon_mnem() == "retn":
            print("hit retn, stopping trace")
            break

        # do uncon jumps
        if insn.get_canon_mnem() == "call" or insn.get_canon_mnem() == "jmp":
            cur_ea = insn.ops[0].addr - length
            if insn.get_canon_mnem() == "jmp":
                if insn.ops[0].type == ida_ua.o_reg:
                    print("hit jmp reg, stopping trace")
                    break

        if insn.get_canon_mnem() != "call" and insn.get_canon_mnem() != "jmp":
            # code.append(ida_bytes.get_bytes(cur_ea, length))
            triton_inst = Instruction(ida_bytes.get_bytes(cur_ea, length))
            code.add(triton_inst)
            rips.append(cur_ea)
            disasm_inst.append(disasm)
            # print(disasm)
            # print( f"recorded {' '.join(f'{b:02x}' for b in ida_bytes.get_bytes(cur_ea, length))}" )
        elif insn.get_canon_mnem() == "call":
            # sub rsp, 8
            # code.append(b"\x48\x83\xec\x08")  # to maintain the effect of call on stack
            triton_inst = Instruction(b"\x48\x83\xec\x08")
            code.add(triton_inst)
            rips.append(cur_ea)
            disasm_inst.append("(call)")

        # else:
        # print(disasm + " (skip)")
        count = count + 1
        cur_ea = cur_ea + length

    # to correctly calculate next handler address (rdi)
    # we have to transfer vip value (rsi) over, as well as its memory regions

    def memory_read_callback_vmhandler(ctx: TritonContext, mem: MemoryAccess):
        addr = mem.getAddress()
        size = mem.getSize()
        if not ctx.isConcreteMemoryValueDefined(addr, size):
            print(f"mem read {hex(addr)}, size {hex(size)} (intercepted)")
            bytes = ida_bytes.get_bytes(addr, size)
            if bytes != None:
                ctx.setConcreteMemoryAreaValue(addr, bytes, False)
                print_bytes(bytes)
            else:
                print(f"failed to read {addr}")
        else:
            print(f"mem read {hex(addr)}, size {hex(size)} (concrete value)")
            bytes = ctx.getConcreteMemoryAreaValue(addr, size, False)
            print_bytes(bytes)

    def memory_write_callback_vmhandler(ctx: TritonContext, mem: MemoryAccess, value):
        addr = mem.getAddress()
        size = mem.getSize()
        print(f"mem write {hex(addr)}, size {hex(size)}, value {hex(value)}")

    ctx.clearCallbacks()
    # simplify before callback is added
    code_s = ctx.simplify(code)
    print(code_s)
    # ctx.disassembly(code_s)
    ctx.addCallback(CALLBACK.GET_CONCRETE_MEMORY_VALUE, memory_read_callback_vmhandler)
    ctx.addCallback(CALLBACK.SET_CONCRETE_MEMORY_VALUE, memory_write_callback_vmhandler)

    ctx.processing(code_s)
    print(hex(ctx.getSymbolicRegisterValue(ctx.registers.rax)))
    print(hex(ctx.getSymbolicRegisterValue(ctx.registers.rbx)))
    print(hex(ctx.getSymbolicRegisterValue(ctx.registers.rdi)))
