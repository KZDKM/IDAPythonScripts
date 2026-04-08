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
vm_enter(idaapi.get_screen_ea(), ctx)
count = 0
while True:
    count = count + 1
    print(
        f"===Start VMHandler{count} at {hex(ctx.getConcreteRegisterValue(ctx.registers.rdi))}==="
    )
    vm_handler(ctx.getConcreteRegisterValue(ctx.registers.rdi), ctx)
