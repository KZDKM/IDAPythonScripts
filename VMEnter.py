import struct

import idaapi
from triton import *


def print_bytes(b):
    print(" ".join(f"{b:02x}" for b in b))


def vm_enter(cur_ea, ctx: TritonContext):
    print("===BEGIN VMENTER===")
    # record esp offset
    esp_off = 0
    stack = []  # stack position and values, only counting immediate
    mappings = []  # stack position and register name, for tracking map
    stack_reads = []  # to associate imm values on stack with regs

    # save executed bytecode for emulation
    code = BasicBlock()

    # strategy: we go as we build a stack and mappings
    # collect bytecodes, run until we hit jmp reg
    # we then use the known values to run unicorn to figure out reg value
    count = 0
    while count < 1000:
        disasm = idaapi.generate_disasm_line(cur_ea, 0)
        disasm = idaapi.tag_remove(disasm)
        insn = idaapi.insn_t()
        length = idaapi.decode_insn(insn, cur_ea)

        if insn.get_canon_mnem() == "ret":
            break

        # do uncon jumps
        if insn.get_canon_mnem() == "call" or insn.get_canon_mnem() == "jmp":
            cur_ea = insn.ops[0].addr - length
            if insn.get_canon_mnem() == "jmp":
                if insn.ops[0].type == idaapi.o_reg:
                    break  # TODO
            if insn.get_canon_mnem() == "call":
                esp_off = esp_off + 8

        if insn.get_canon_mnem() == "pushfq":
            esp_off = esp_off + 8

        if insn.get_canon_mnem() == "push":
            esp_off = esp_off + 8
            if insn.ops[0].type == idaapi.o_reg:
                mappings.append((idaapi.get_reg_name(insn.ops[0].reg, 8), esp_off))
            # we push imms onto virtual stack
            if insn.ops[0].type == idaapi.o_imm:
                stack.append((esp_off, insn.ops[0].value))

        # TODO: remove mapping if popped
        if insn.get_canon_mnem() == "pop":
            mappings.pop()
            esp_off = esp_off - 8

        # check stack access
        if insn.get_canon_mnem() == "mov":
            if insn.ops[1].type == idaapi.o_displ:
                if idaapi.get_reg_name(insn.ops[1].reg, 8) == "rsp":
                    stack_reads.append(
                        (
                            esp_off - insn.ops[1].addr,
                            idaapi.get_reg_name(insn.ops[0].reg, 8),
                        )
                    )

        if insn.get_canon_mnem() != "call" and insn.get_canon_mnem() != "jmp":
            # replace rip reads
            triton_inst = Instruction(idaapi.get_bytes(cur_ea, length))
            triton_inst.setAddress(cur_ea)
            if disasm.startswith("lea"):
                if insn.ops[1].type == idaapi.o_mem:
                    dest_reg = insn.ops[0].reg
                    # holy shitshow: movabs reg, addr
                    instruction_bytes = struct.pack(
                        "<BBQ",
                        0x49 if dest_reg > 7 else 0x48,
                        0xB8 + (dest_reg & 7),
                        insn.ops[1].addr,
                    )
                    triton_inst = Instruction(instruction_bytes)
                    print("------")
                    print("Following instruction replaced: ")
                    print_bytes(instruction_bytes)
                    ctx.disassembly(triton_inst)
                    print(triton_inst.getDisassembly())
                    print("------")

            code.add(triton_inst)
            print(disasm)
            # print( f"recorded {' '.join(f'{b:02x}' for b in ida_bytes.get_bytes(cur_ea, length))}" )
        elif insn.get_canon_mnem() == "call":
            # sub rsp, 8
            triton_inst = Instruction(b"\x48\x83\xec\x08")
            triton_inst.setAddress(cur_ea)
            code.add(triton_inst)  # to maintain the effect of call on stack
            print("(call)")

        else:
            print(disasm + " (skip)")
        count = count + 1
        cur_ea = cur_ea + length

    print("Stack operations:")
    for m in mappings:
        print("[esp + " + hex(esp_off - m[1]) + "] -> " + m[0])
    for s in stack:
        print("[esp + " + hex(esp_off - s[0]) + "] = " + hex(s[1]))
    for r in stack_reads:
        print(r[1] + " = " + "[esp + " + hex(esp_off - r[0]) + "]")

    print("Simplified trace:")
    ctx.clearCallbacks()
    code_s = ctx.simplify(code)
    print(code_s)

    def memory_read_callback_vmenter(ctx: TritonContext, mem: MemoryAccess):
        addr = mem.getAddress()
        size = mem.getSize()
        rsp = ctx.getConcreteRegisterValue(ctx.registers.rsp)
        # check if access is on stack, jank
        if rsp <= addr < rsp + 0x1000:
            print(f"stack access {hex(addr)} -> [rsp + {hex(addr - rsp)}]: ")
            print_bytes(ctx.getConcreteMemoryAreaValue(addr, 8))
            return
        b = idaapi.get_bytes(addr, size)
        ctx.setConcreteMemoryAreaValue(addr, b)
        print(f"mem accessed at {hex(addr)}:")
        print_bytes(b)

    def memory_write_callback_vmenter(ctx: TritonContext, mem: MemoryAccess, value):
        addr = mem.getAddress()
        size = mem.getSize()
        print(f"mem write {hex(addr)}, size {hex(size)}, value {hex(value)}")

    ctx.setConcreteRegisterValue(ctx.registers.rsp, 0x20000)
    ctx.addCallback(CALLBACK.GET_CONCRETE_MEMORY_VALUE, memory_read_callback_vmenter)
    ctx.addCallback(CALLBACK.SET_CONCRETE_MEMORY_VALUE, memory_write_callback_vmenter)
    ctx.processing(code_s)
    print(hex(ctx.getSymbolicRegisterValue(ctx.registers.rax)))
    print(f"ebx: {hex(ctx.getConcreteRegisterValue(ctx.registers.rbx))}")
    print(f"jump target: {hex(ctx.getConcreteRegisterValue(ctx.registers.rdi))}")
    print("===END VMENTER===")
