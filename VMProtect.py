import importlib
import sys

sys.dont_write_bytecode = True

import idaapi
from triton import *

from VMEnter import vm_enter
from VMHandler import vm_handler

importlib.reload(sys.modules["VMEnter"])
importlib.reload(sys.modules["VMHandler"])


idaapi.msg_clear()
idaapi.init_hexrays_plugin()
ctx = TritonContext(ARCH.X86_64)

ctx.symbolizeRegister(ctx.registers.rax, "rax_i")
ctx.symbolizeRegister(ctx.registers.rcx, "rcx_i")
ctx.symbolizeRegister(ctx.registers.rdx, "rdx_i")
ctx.symbolizeRegister(ctx.registers.rbx, "rbx_i")
ctx.symbolizeRegister(ctx.registers.rsp, "rsp_i")
ctx.symbolizeRegister(ctx.registers.rbp, "rbp_i")
ctx.symbolizeRegister(ctx.registers.rsi, "rsi_i")
ctx.symbolizeRegister(ctx.registers.rdi, "rdi_i")
ctx.symbolizeRegister(ctx.registers.r8, "r8_i")
ctx.symbolizeRegister(ctx.registers.r9, "r9_i")
ctx.symbolizeRegister(ctx.registers.r10, "r10_i")
ctx.symbolizeRegister(ctx.registers.r11, "r11_i")
ctx.symbolizeRegister(ctx.registers.r12, "r12_i")
ctx.symbolizeRegister(ctx.registers.r13, "r13_i")
ctx.symbolizeRegister(ctx.registers.r14, "r14_i")
ctx.symbolizeRegister(ctx.registers.r15, "r15_i")

vm_enter(idaapi.get_screen_ea(), ctx)
count = 0
while True:
    count = count + 1
    if ctx.getConcreteRegisterValue(ctx.registers.rdi) > 0x200000000:
        print("===Reached VMExit===")
        break
    print(
        f"===Start VMHandler{count} at {hex(ctx.getConcreteRegisterValue(ctx.registers.rdi))}==="
    )
    vm_handler(ctx.getConcreteRegisterValue(ctx.registers.rdi), ctx)

print(ctx.liftToLLVM(ctx.getSymbolicRegister(ctx.registers.rax)))
