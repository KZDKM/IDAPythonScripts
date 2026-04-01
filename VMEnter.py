import idaapi
import idautils
import idc
import ida_hexrays
import ida_ua
import ida_kernwin
import idaapi
import ida_bytes

import math

from unicorn import *
from unicorn.x86_const import *

ida_hexrays.init_hexrays_plugin()
ida_kernwin.msg_clear()

# start at vm enter
cur_ea = 0x1400fbc08
# record esp offset
esp_off = 0
stack = [] # stack position and values, only counting immediate
mappings = [] # stack position and register name, for tracking map
stack_reads = [] # to associate imm values on stack with regs

# save executed bytecode
code = []

# get value from virtual stack
def stack_get(off):
    for s in stack:
        if s[0] == off:
            return s[1]
    return None

# strategy: we go as we build a stack and mappings
# collect bytecodes, run until we hit jmp reg
# we then use the known values to run unicorn to figure out reg value
count = 0
while count < 1:
    disasm = idc.generate_disasm_line(cur_ea, 0)
    print(disasm)
    insn = ida_ua.insn_t()
    length = ida_ua.decode_insn(insn, cur_ea)

    if insn.get_canon_mnem() == "ret":
        break

    # do uncon jumps
    if insn.get_canon_mnem() == "call" or insn.get_canon_mnem() == "jmp":
        cur_ea = insn.ops[0].addr - length
        if insn.get_canon_mnem() == "jmp":
            if insn.ops[0].type == ida_ua.o_reg:
                break # TODO
        if insn.get_canon_mnem() == "call":
            esp_off = esp_off + 8

    if insn.get_canon_mnem() == "pushfq":
        esp_off = esp_off + 8 

    if insn.get_canon_mnem() == "push":
        esp_off = esp_off + 8 
        if insn.ops[0].type == ida_ua.o_reg:
            mappings.append((idaapi.get_reg_name(insn.ops[0].reg,8), esp_off))
        # we push imms onto virtual stack
        if insn.ops[0].type == ida_ua.o_imm:
            stack.append((esp_off, insn.ops[0].value))

    # check stack access
    if insn.get_canon_mnem() == "mov":
        if insn.ops[1].type == ida_ua.o_displ:
            if idaapi.get_reg_name(insn.ops[1].reg, 8) == "rsp":
                stack_reads.append((esp_off - insn.ops[1].addr, idaapi.get_reg_name(insn.ops[0].reg,8)))

    if insn.get_canon_mnem() != "call" and insn.get_canon_mnem() != "jmp":
        code.append(ida_bytes.get_bytes(cur_ea, length))
    count = count + 1
    cur_ea = cur_ea + length

print("Stack operations:")
for m in mappings:
    print("[esp + " + str(esp_off - m[1]) + "] -> " + m[0])
for s in stack:
    print("[esp + " + str(esp_off - s[0]) + "] = " + hex(s[1]))
for r in stack_reads:
    print(r[1] + " = " + "[esp + " + str(esp_off - r[0]) + "]")

def hook_mem_read(uc, access, address, size, value, user_data):
    esp = uc.reg_read(UC_X86_REG_ESP)
    if esp <= address < esp + 0x100:
        val = stack_get(esp)
        if val != None:
            print(str(address) + " -> " + str(val))
            uc.mem_write(address, val)
def hook_mem_write(uc, access, address, size, value, user_data):
    rip = uc.reg_read(UC_X86_REG_RIP)
    uc.reg_write(UC_X86_REG_RIP, rip + size)

print("collected " + str(b''.join(code).__len__()) + " bytes of code")
mu = Uc(UC_ARCH_X86, UC_MODE_64)
mu.mem_map(0x1000000, 2 * 1024 * 1024)
mu.mem_write(0x1000000, b''.join(code))
mu.hook_add(UC_HOOK_MEM_READ, hook_mem_read)
mu.hook_add(UC_HOOK_MEM_WRITE, hook_mem_write)

def hook_invalid(uc, access, address, size, value, user_data):
    print(f"INVALID access at {hex(address)}")
    return False  # stop emulation

mu.hook_add(UC_HOOK_MEM_INVALID, hook_invalid)

mu.mem_map(0x2000000, 0x1000)
mu.reg_write(UC_X86_REG_RSP, 0x2001000)

import platform
print(platform.machine())
#mu.emu_start(0x1000000, 0x1000000 + b''.join(code).__len__())
