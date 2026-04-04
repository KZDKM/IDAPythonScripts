import ida_bytes
import ida_hexrays
import ida_kernwin
import ida_ua
import idaapi
import idc
from unicorn import *
from unicorn.x86_const import *

ida_hexrays.init_hexrays_plugin()
ida_kernwin.msg_clear()

# start at vm enter
cur_ea = idaapi.get_screen_ea()
# record esp offset
esp_off = 0
stack = []  # stack position and values, only counting immediate
mappings = []  # stack position and register name, for tracking map
stack_reads = []  # to associate imm values on stack with regs
rips = []  # record rip values
disasm_inst = []  # save disassembled instructions

# save executed bytecode for emulation
code = []


# get value from virtual stack
def stack_get(off):
    for s in stack:
        if s[0] == off:
            return s[1]
    return None


# get reg from mapping
def mapping_get(off):
    for m in mappings:
        if m[1] == off:
            return m[0]
    return None


def print_bytes(b):
    print(" ".join(f"{b:02x}" for b in b))


# strategy: we go as we build a stack and mappings
# collect bytecodes, run until we hit jmp reg
# we then use the known values to run unicorn to figure out reg value
count = 0
while count < 1000:
    disasm = idc.generate_disasm_line(cur_ea, 0)
    insn = ida_ua.insn_t()
    length = ida_ua.decode_insn(insn, cur_ea)

    if insn.get_canon_mnem() == "ret":
        break

    # do uncon jumps
    if insn.get_canon_mnem() == "call" or insn.get_canon_mnem() == "jmp":
        cur_ea = insn.ops[0].addr - length
        if insn.get_canon_mnem() == "jmp":
            if insn.ops[0].type == ida_ua.o_reg:
                break  # TODO
        if insn.get_canon_mnem() == "call":
            esp_off = esp_off + 8

    if insn.get_canon_mnem() == "pushfq":
        esp_off = esp_off + 8

    if insn.get_canon_mnem() == "push":
        esp_off = esp_off + 8
        if insn.ops[0].type == ida_ua.o_reg:
            mappings.append((idaapi.get_reg_name(insn.ops[0].reg, 8), esp_off))
        # we push imms onto virtual stack
        if insn.ops[0].type == ida_ua.o_imm:
            stack.append((esp_off, insn.ops[0].value))

    # TODO: remove mapping if popped

    # check stack access
    if insn.get_canon_mnem() == "mov":
        if insn.ops[1].type == ida_ua.o_displ:
            if idaapi.get_reg_name(insn.ops[1].reg, 8) == "rsp":
                stack_reads.append(
                    (
                        esp_off - insn.ops[1].addr,
                        idaapi.get_reg_name(insn.ops[0].reg, 8),
                    )
                )

    if insn.get_canon_mnem() != "call" and insn.get_canon_mnem() != "jmp":
        code.append(ida_bytes.get_bytes(cur_ea, length))
        rips.append(cur_ea)
        disasm_inst.append(disasm)
        print(disasm)
        # print( f"recorded {' '.join(f'{b:02x}' for b in ida_bytes.get_bytes(cur_ea, length))}" )
    elif insn.get_canon_mnem() == "call":
        # sub rsp, 8
        code.append(b"\x48\x83\xec\x08")  # to maintain the effect of call on stack
        rips.append(cur_ea)
        disasm_inst.append("(call)")

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


# sanity check for emulation
print("collected " + str(b"".join(code).__len__()) + " bytes of code")
print(f"recorded {' '.join(f'{b:02x}' for b in b''.join(code))}")

stack_start = 0x2000000
stack_size = 0x5000
image_start = 0x140000000
image_size = 0x100000
mu = Uc(UC_ARCH_X86, UC_MODE_64)
mu.mem_map(stack_start, stack_size)  # initialize a dummy stack
mu.mem_map(image_start, image_size)
mu.reg_write(UC_X86_REG_RSP, stack_start + stack_size - 8)


def hook_mem_read(uc, access, address, size, value, user_data):
    rsp = uc.reg_read(UC_X86_REG_RSP)
    print("mem read " + hex(address))
    # stack read
    if stack_start <= address < stack_start + stack_size:
        val = stack_get((stack_start + stack_size - 8) - address)
        print(f"try get {hex((stack_start + stack_size - 8) - address)} on stack")
        if val != None:
            print("stack read")
            print(hex(address) + " -> " + hex(val))
            uc.mem_write(address, val.to_bytes(8, byteorder="little"))
            print_bytes(uc.mem_read(address, 8))
            return
        reg = mapping_get((stack_start + stack_size - 8) - address)
        if reg != None:
            print(
                f"stack read {hex((stack_start + stack_size - 8) - address)} -> {reg}"
            )
            return
        print("did not find on stack")
        return
    # simulate read to data
    b = idc.get_bytes(address, size)
    print("mem accessed:")
    print_bytes(b)
    uc.mem_write(address, b)


# halt on invalid mem access
def hook_invalid(uc, access, address, size, value, user_data):
    print(f"INVALID memory access at {hex(address)}")
    return False  # stop emulation


def hook_code(uc, address, size, user_data):
    if not hasattr(hook_code, "count"):
        hook_code.count = 0
    # print(f"line {hook_code.count}")
    inst_bytes = uc.mem_read(address, size)
    # hex_str = " ".join(f"{b:02x}" for b in inst_bytes)
    # print(f"RIP {hex(address)}")
    # print(hex_str)
    print(disasm_inst[hook_code.count])

    if inst_bytes.startswith(b"\x48\x8d\x3d"):  # lea rdi, [rip + disp32]
        # Calculate original target
        disp = int.from_bytes(uc.mem_read(address + 3, 4), "little", signed=True)
        next_rip = address + 7
        original_addr = rips[hook_code.count] + 7 + disp

        # Replace with your value
        uc.reg_write(UC_X86_REG_RDI, original_addr)

        # Skip the lea instruction (emulate its effect manually)
        uc.reg_write(UC_X86_REG_RIP, next_rip)
        return
    hook_code.count += 1


mu.mem_map(0x1000000, 2 * 1024 * 1024)
mu.mem_write(0x1000000, b"".join(code))
mu.hook_add(UC_HOOK_MEM_READ, hook_mem_read)
mu.hook_add(UC_HOOK_CODE, hook_code)
mu.hook_add(UC_HOOK_MEM_INVALID, hook_invalid)

mu.emu_start(0x1000000, 0x1000000 + b"".join(code).__len__())
# todo: support dynamic target registers
print(f"jump target: {hex(mu.reg_read(UC_X86_REG_RDI))}")
