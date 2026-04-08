import ida_bytes
import ida_ua
import idaapi
import idc
from triton import *


def print_bytes(b):
    print(" ".join(f"{b:02x}" for b in b))


def vm_handler(cur_ea, ctx: TritonContext):

    code = BasicBlock()
    # somehow the first instruction in a new basicblock has wrong address
    code.add(
        Instruction(b"\x90")
    )  # hack fix, have no idea what the actual fuck is going on

    inst_count = 0
    while True:
        disasm = idc.generate_disasm_line(cur_ea, 0)
        disasm = idaapi.tag_remove(disasm)
        inst = ida_ua.insn_t()
        length = ida_ua.decode_insn(inst, cur_ea)

        if inst.get_canon_mnem() == "retn":
            print("hit retn, stopping trace")
            break

        # do uncon jumps
        if inst.get_canon_mnem() == "call" or inst.get_canon_mnem() == "jmp":
            cur_ea = inst.ops[0].addr
            # detect dynamic jump
            if inst.get_canon_mnem() == "jmp":
                if inst.ops[0].type == ida_ua.o_reg:
                    print("hit jmp reg, stopping trace")
                    break
            # to maintain the effect of call on stack
            if inst.get_canon_mnem() == "call":
                # sub rsp, 8
                triton_inst = Instruction(b"\x48\x83\xec\x08")
                ctx.processing(triton_inst)
                code.add(triton_inst)

            inst_count = inst_count + 1
            continue

        triton_inst = Instruction(ida_bytes.get_bytes(cur_ea, length))
        ctx.disassembly(triton_inst)

        # resolve opaque predicate
        if triton_inst.isBranch():
            # print(disasm)
            ctx.processing(triton_inst)
            pred = ctx.getPathPredicate()
            print(f"solving opaque predicate {pred}")
            ast_ctx = ctx.getAstContext()
            model = ctx.getModel(ast_ctx.lnot(pred))
            if model:
                print("ERROR: found indeterminate branch")
            else:
                print(f"branch taken {triton_inst.isConditionTaken()}")
                if triton_inst.isConditionTaken():
                    cur_ea = inst.ops[0].addr
                    inst_count = inst_count + 1
                    continue
        else:
            code.add(triton_inst)
            ctx.processing(triton_inst)
            # print(disasm)

        inst_count = inst_count + 1
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

    # ctx.processing(code_s)
    # print(hex(ctx.getSymbolicRegisterValue(ctx.registers.rax)))
    # print(hex(ctx.getSymbolicRegisterValue(ctx.registers.rbx)))
    # print(hex(ctx.getSymbolicRegisterValue(ctx.registers.rdi)))
