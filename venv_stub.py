import sys
from pathlib import Path

import ida_venv

sys.dont_write_bytecode = True

venv_path = Path(Path.home(), ".idapro", "venv")
# create the venv
ida_venv.create_venv(venv_path)
# activate the venv
ida_venv.activate_venv(venv_path)
exec(open("./VMProtect.py").read())
