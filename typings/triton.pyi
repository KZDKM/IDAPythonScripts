from typing import List, Union, Callable, Tuple, Any
from typing_extensions import Self
from enum import IntEnum



class SymbolicVariable:
    def __init__(self, *args, **kargs):
        pass


    def getAlias(self, ):
        # type: (Self) -> str
        """Returns the alias (if exists) of the symbolic variable."""
        pass


    def getBitSize(self, ):
        # type: (Self) -> int
        """Returns the size of the symbolic variable."""
        pass


    def getComment(self, ):
        # type: (Self) -> str
        """Returns the comment (if exists) of the symbolic variable."""
        pass


    def getId(self, ):
        # type: (Self) -> int
        """Returns the id of the symbolic variable. This id is always unique.<br>
e.g: `18`"""
        pass


    def getName(self, ):
        # type: (Self) -> str
        """Returns name of the symbolic variable.<br>
e.g: `SymVar_18`"""
        pass


    def getOrigin(self, ):
        # type: (Self) -> int
        """Returns the origin according to the SYMBOLIC value.<br>
If `getType()` returns triton::engines::symbolic::REGISTER_VARIABLE, then `getOrigin()` returns the id of the register.<br>
Otherwise, if `getType()` returns triton::engines::symbolic::MEMORY_VARIABLE, then `getOrigin()` returns the address of the memory access.<br>
Then, if `getType()` returns triton::engines::symbolic::UNDEFINED_VARIABLE, then `getOrigin()` returns `0`."""
        pass


    def getType(self, ):
        # type: (Self) -> SYMBOLIC
        """Returns the type of the symbolic variable.<br>
e.g: `SYMBOLIC.REGISTER_VARIABLE`"""
        pass


    def setAlias(self, comment):
        # type: (Self, str) -> None
        """Sets an alias to the symbolic variable."""
        pass


    def setComment(self, comment):
        # type: (Self, str) -> None
        """Sets a comment to the symbolic variable."""
        pass




class AstContext:
    def __init__(self, *args, **kargs):
        pass


    def array(self, addrSize):
        # type: (Self, int) -> AstNode
        """Creates an `array` node.<br>
e.g: `(Array (_ BitVec addrSize) (_ BitVec 8))`."""
        pass


    def assert_(self, node):
        # type: (Self, AstNode) -> AstNode
        """Creates a `assert` node.
e.g: `(assert node)`."""
        pass


    def bswap(self, node):
        # type: (Self, AstNode) -> AstNode
        """Creates a `bswap` node.
e.g: `(bswap node)`."""
        pass


    def bv(self, value, size):
        # type: (Self, int, int) -> AstNode
        """Creates a `bv` node (bitvector). The `size` must be in bits.<br>
e.g: `(_ bv<balue> size)`."""
        pass


    def bvadd(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvadd` node.<br>
e.g: `(bvadd node1 epxr2)`."""
        pass


    def bvand(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvand` node.<br>
e.g: `(bvand node1 epxr2)`."""
        pass


    def bvashr(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvashr` node (arithmetic shift right).<br>
e.g: `(bvashr node1 epxr2)`."""
        pass


    def bvfalse(self, ):
        # type: (Self) -> AstNode
        """This is an alias on the `(_ bv0 1)` ast expression."""
        pass


    def bvlshr(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvlshr` node (logical shift right).<br>
e.g: `(lshr node1 epxr2)`."""
        pass


    def bvmul(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvmul` node.<br>
e.g: `(bvmul node1 node2)`."""
        pass


    def bvnand(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvnand` node.<br>
e.g: `(bvnand node1 node2)`."""
        pass


    def bvneg(self, node1):
        # type: (Self, AstNode) -> AstNode
        """Creates a `bvneg` node.<br>
e.g: `(bvneg node1)`."""
        pass


    def bvnor(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvnor` node.<br>
e.g: `(bvnor node1 node2)`."""
        pass


    def bvnot(self, node1):
        # type: (Self, AstNode) -> AstNode
        """Creates a `bvnot` node.<br>
e.g: `(bvnot node1)`."""
        pass


    def bvor(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvor` node.<br>
e.g: `(bvor node1 node2)`."""
        pass


    def bvror(self, node, rot):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvror` node (rotate right).<br>
e.g: `((_ rotate_right rot) node)`."""
        pass


    def bvrol(self, node, rot):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvrol` node (rotate left).<br>
e.g: `((_ rotate_left rot) node)`."""
        pass


    def bvsdiv(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvsdiv` node.<br>
e.g: `(bvsdiv node1 epxr2)`."""
        pass


    def bvsge(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvsge` node.<br>
e.g: `(bvsge node1 epxr2)`."""
        pass


    def bvsgt(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvsgt` node.<br>
e.g: `(bvsgt node1 epxr2)`."""
        pass


    def bvshl(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a Bvshl node (shift left).<br>
e.g: `(bvshl node1 node2)`."""
        pass


    def bvsle(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvsle` node.<br>
e.g: `(bvsle node1 epxr2)`."""
        pass


    def bvslt(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvslt` node.<br>
e.g: `(bvslt node1 epxr2)`."""
        pass


    def bvsmod(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvsmod` node (2's complement signed remainder, sign follows divisor).<br>
e.g: `(bvsmod node1 node2)`."""
        pass


    def bvsrem(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvsrem` node (2's complement signed remainder, sign follows dividend).<br>
e.g: `(bvsrem node1 node2)`."""
        pass


    def bvsub(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvsub` node.<br>
e.g: `(bvsub node1 epxr2)`."""
        pass


    def bvtrue(self, ):
        # type: (Self) -> AstNode
        """This is an alias on the `(_ bv1 1)` ast expression.<br>"""
        pass


    def bvudiv(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvudiv` node.<br>
e.g: `(bvudiv node1 epxr2)`."""
        pass


    def bvuge(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvuge` node.<br>
e.g: `(bvuge node1 epxr2)`."""
        pass


    def bvugt(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvugt` node.<br>
e.g: `(bvugt node1 epxr2)`."""
        pass


    def bvule(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvule` node.<br>
e.g: `(bvule node1 epxr2)`."""
        pass


    def bvult(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvult` node.<br>
e.g: `(bvult node1 epxr2)`."""
        pass


    def bvurem(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvurem` node (unsigned remainder).<br>
e.g: `(bvurem node1 node2)`."""
        pass


    def bvxnor(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvxnor` node.<br>
e.g: `(bvxnor node1 node2)`."""
        pass


    def bvxor(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `bvxor` node.<br>
e.g: `(bvxor node1 epxr2)`."""
        pass


    def concat(self, args):
        # type: (Self, List[AstNode]) -> AstNode
        """Concatenates several nodes."""
        pass


    def declare(self, sort):
        # type: (Self, AstNode) -> AstNode
        """Declare a function without argument. Mainly used to delcare a variable or an array.<br>
e.g: `(declare-fun SymVar_0 () (_ BitVec 64))`"""
        pass


    def distinct(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `distinct` node.<br>
e.g: `(distinct node1 node2)`"""
        pass


    def equal(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates an `equal` node.<br>
e.g: `(= node1 epxr2)`."""
        pass


    def extract(self, high, low, node1):
        # type: (Self, int, int, AstNode) -> AstNode
        """Creates an `extract` node. The `high` and `low` fields represent the bits position.<br>
e.g: `((_ extract high low) node1)`."""
        pass


    def forall(self, args, body):
        # type: (Self, List[AstNode], AstNode) -> AstNode
        """Creates an `forall` node.<br>
e.g: `(forall ((x (_ BitVec <size>)), ...) body)`."""
        pass


    def iff(self, node1, node2):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates an `iff` node (if and only if).<br>
e.g: `(iff node1 node2)`."""
        pass


    def ite(self, ifExpr, thenExpr, elseExpr):
        # type: (Self, AstNode, AstNode, AstNode) -> AstNode
        """Creates an `ite` node (if-then-else node).<br>
e.g: `(ite ifExpr thenExpr elseExpr)`."""
        pass


    def land(self, args):
        # type: (Self, List[AstNode]) -> AstNode
        """Creates a logical `AND` on several nodes.
e.g: `(and node1 node2 node3 node4)`."""
        pass


    def let(self, alias, node2, node3):
        # type: (Self, str, AstNode, AstNode) -> AstNode
        """Creates a `let` node.<br>
e.g: `(let ((alias node2)) node3)`."""
        pass


    def lnot(self, node):
        # type: (Self, AstNode) -> AstNode
        """Creates a `lnot` node (logical NOT).<br>
e.g: `(not node)`."""
        pass


    def lor(self, args):
        # type: (Self, List[AstNode]) -> AstNode
        """Creates a logical `OR` on several nodes.
e.g: `(or node1 node2 node3 node4)`."""
        pass


    def lxor(self, args):
        # type: (Self, List[AstNode]) -> AstNode
        """Creates a logical `XOR` on several nodes.
e.g: `(xor node1 node2 node3 node4)`."""
        pass


    def reference(self, expr):
        # type: (Self, SymbolicExpression) -> AstNode
        """Creates a reference node (SSA-based).<br>
e.g: `ref!123`."""
        pass


    def select(self, array, index):
        # type: (Self, AstNode, AstNode) -> AstNode
        """Creates a `select` node.<br>
e.g: `(select array index)`."""
        pass


    def store(self, array, index, expr):
        # type: (Self, AstNode, AstNode, AstNode) -> AstNode
        """Creates a `store` node.<br>
e.g: `(store array index expr)`."""
        pass


    def string(self, s):
        # type: (Self, str) -> AstNode
        """Creates a `string` node."""
        pass


    def sx(self, sizeExt, node1):
        # type: (Self, int, AstNode) -> AstNode
        """Creates a `sx` node (sign extend).<br>
e.g: `((_ sign_extend sizeExt) node1)`."""
        pass


    def variable(self, symVar):
        # type: (Self, SymbolicVariable) -> AstNode
        """Creates a `variable` node."""
        pass


    def zx(self, sizeExt, node1):
        # type: (Self, int, AstNode) -> AstNode
        """Creates a `zx` node (zero extend).<br>
e.g: `((_ zero_extend sizeExt) node1)`."""
        pass


    def dereference(self, node):
        # type: (Self, AstNode) -> AstNode
        """Returns the first non referene node encountered."""
        pass


    def duplicate(self, node):
        # type: (Self, AstNode) -> AstNode
        """Duplicates the node and returns a new instance as AstNode."""
        pass


    def search(self, node, match):
        # type: (Self, AstNode, AST_NODE) -> List[AstNode]
        """Returns a list of collected matched nodes via a depth-first pre order traversal."""
        pass


    def tritonToZ3(self, node):
        # type: (Self, AstNode) -> z3.ExprRef
        """Convert a Triton AST to a Z3 AST."""
        pass


    def unroll(self, node):
        # type: (Self, AstNode) -> AstNode
        """Unrolls the SSA form of a given AST."""
        pass


    def z3ToTriton(self, expr):
        # type: (Self, z3.ExprRef) -> AstNode
        """Convert a Z3 AST to a Triton AST."""
        pass




class AstNode:
    def __init__(self, *args, **kargs):
        pass


    def equalTo(self, args):
        # type: (Self, AstNode) -> bool
        """Compares the current tree to another one."""
        pass


    def evaluate(self, ):
        # type: (Self) -> int
        """Evaluates the tree and returns its value."""
        pass


    def getBitvectorMask(self, ):
        # type: (Self) -> int
        """Returns the mask of the node vector according to its size.<br>
e.g: `0xffffffff`"""
        pass


    def getBitvectorSize(self, ):
        # type: (Self) -> int
        """Returns the node vector size."""
        pass


    def getChildren(self, ):
        # type: (Self) -> List[AstNode]
        """Returns the list of child nodes."""
        pass


    def getHash(self, ):
        # type: (Self) -> int
        """Returns the hash (signature) of the AST."""
        pass


    def getInteger(self, ):
        # type: (Self) -> int
        """Returns the integer of the node. Only available on `INTEGER_NODE`, raises an exception otherwise."""
        pass


    def getLevel(self, ):
        # type: (Self) -> int
        """Returns the deep level of the AST."""
        pass


    def getParents(self, ):
        # type: (Self) -> List[AstNode]
        """Returns the parents list nodes. The list is empty if there is no parent defined yet."""
        pass


    def getString(self, ):
        # type: (Self) -> str
        """Returns the string of the node. Only available on `STRING_NODE`, raises an exception otherwise."""
        pass


    def getSymbolicExpression(self, ):
        # type: (Self) -> SymbolicExpression
        """Returns the symbolic expression of the node. Only available on `REFERENCE_NODE`, raises an exception otherwise."""
        pass


    def getSymbolicVariable(self, ):
        # type: (Self) -> SymbolicVariable
        """Returns the symbolic variable of the node. Only available on `VARIABLE_NODE`, raises an exception otherwise."""
        pass


    def getType(self, ):
        # type: (Self) -> AST_NODE
        """Returns the type of the node.<br>
e.g: `AST_NODE.BVADD`"""
        pass


    def isArray(self, ):
        # type: (Self) -> bool
        """Returns true if it's an array node.
e.g: `AST_NODE.ARRAY` and `AST_NODE.STORE`."""
        pass


    def isLogical(self, ):
        # type: (Self) -> bool
        """Returns true if it's a logical node.
e.g: `AST_NODE.EQUAL`, `AST_NODE.LNOT`, `AST_NODE.LAND`..."""
        pass


    def isSigned(self, ):
        # type: (Self) -> bool
        """According to the size of the expression, returns true if the MSB is 1."""
        pass


    def isSymbolized(self, ):
        # type: (Self) -> bool
        """Returns true if the tree (and its sub-trees) contains a symbolic variable."""
        pass


    def setChild(self, index, node):
        # type: (Self, int, AstNode) -> None
        """Replaces a child node."""
        pass




class Register:
    def __init__(self, *args, **kargs):
        pass


    def getBitSize(self, ):
        # type: (Self) -> int
        """Returns the size (in bits) of the register.<br>
e.g: `64`"""
        pass


    def getBitvector(self, ):
        # type: (Self) -> BitsVector
        """Returns the bit vector of the register."""
        pass


    def getExtendSize(self, ):
        # type: (Self) -> EXTEND
        """Returns the size (in bits) of the extend. Mainly used for AArch64.<br>
e.g: `16`"""
        pass


    def getExtendType(self, ):
        # type: (Self) -> EXTEND
        """Returns the extend type of the operand. Mainly used for AArch64.<br>
e.g: `EXTEND.ARM.UXTW`"""
        pass


    def getId(self, ):
        # type: (Self) -> REG
        """Returns the enum of the register.<br>
e.g: `REG.X86_64.RBX`"""
        pass


    def getName(self, ):
        # type: (Self) -> str
        """Returns the name of the register.<br>
e.g: `rbx`"""
        pass


    def getShiftType(self, ):
        # type: (Self) -> SHIFT
        """Returns the shift type of the operand. Mainly used for AArch64.<br>
e.g: `SHIFT.ARM.LSL`"""
        pass


    def getShiftImmediate(self, ):
        # type: (Self) -> int
        """Returns the shift immediate value of the operand. Mainly used for AArch64 and ARM32.<br>
e.g: `2`"""
        pass


    def getShiftRegister(self, ):
        # type: (Self) -> REG
        """Returns the shift register of the operand. Mainly used for ARM32.<br>
e.g: `REG.ARM32.R0`"""
        pass


    def getSize(self, ):
        # type: (Self) -> int
        """Returns the size (in bytes) of the register.<br>
e.g: `8`"""
        pass


    def getType(self, ):
        # type: (Self) -> OPERAND
        """Returns the type of the register. In this case this function returns `OPERAND.REG`."""
        pass


    def getVASType(self, ):
        # type: (Self) -> VAS
        """Returns the vector arrangement specifier. Mainly used for AArch64.<br>
e.g: `VAS.ARM.v8B`"""
        pass


    def isMutable(self, ):
        # type: (Self) -> bool
        """Returns true if this register is mutable. Mainly used in AArch64 to define that some registers like XZR are immutable."""
        pass


    def isOverlapWith(self, other):
        # type: (Self, Register) -> bool
        """Returns true if `other` and `self` overlap."""
        pass




class BasicBlock:
    def __init__(self, *args, **kargs):
        pass


    def add(self, inst):
        # type: (Self, Instruction) -> None
        """Adds an instruction to the block."""
        pass


    def getFirstAddress(self, ):
        # type: (Self) -> int
        """Returns the first instruction's address of the block."""
        pass


    def getInstructions(self, ):
        # type: (Self) -> List[Instruction]
        """Returns all instructions of the block."""
        pass


    def getLastAddress(self, ):
        # type: (Self) -> int
        """Returns the last instruction's address of the block."""
        pass


    def getSize(self, ):
        # type: (Self) -> int
        """Returns the number of instruction in the block."""
        pass


    def remove(self, position):
        # type: (Self, int) -> bool
        """Removes the instruction in the block at a given position. Returns true if successed."""
        pass




class PathConstraint:
    def __init__(self, *args, **kargs):
        pass


    def getBranchConstraints(self, ):
        # type: (Self) -> dict
        """Returns the branch constraints as list of dictionary `{isTaken, srcAddr, dstAddr, constraint}`. The source address is the location
of the branch instruction and the destination address is the destination of the jump. E.g: `"0x11223344: jne 0x55667788"`, 0x11223344
is the source address and 0x55667788 is the destination if and only if the branch is taken, otherwise the destination is the next
instruction address."""
        pass


    def getComment(self, ):
        # type: (Self) -> str
        """Returns the comment (if exists) of the path constraint."""
        pass


    def getSourceAddress(self, ):
        # type: (Self) -> int
        """Returns the source address of the branch."""
        pass


    def getTakenAddress(self, ):
        # type: (Self) -> int
        """Returns the address of the taken branch."""
        pass


    def getTakenPredicate(self, ):
        # type: (Self) -> AstNode
        """Returns the predicate of the taken branch."""
        pass


    def getThreadId(self, ):
        # type: (Self) -> int
        """Returns the thread id of the constraint. Returns -1 if thread id is undefined."""
        pass


    def isMultipleBranches(self, ):
        # type: (Self) -> bool
        """Returns true if it is not a direct jump."""
        pass


    def setComment(self, comment):
        # type: (Self, str) -> None
        """Sets comment of the path constraint."""
        pass




class TritonContext:
    def __init__(self, *args, **kargs):
        self.registers = None # type: Any


    def addCallback(self, kind, cb):
        # type: (Self, CALLBACK, Callable) -> None
        """Adds a callback at specific internal points. Your callback will be called each time the point is reached."""
        pass


    def assignSymbolicExpressionToMemory(self, symExpr, mem):
        # type: (Self, SymbolicExpression, MemoryAccess) -> None
        """Assigns a SymbolicExpression to a MemoryAccess area. **Be careful**, use this function only if you know what you are doing.
The symbolic expression (`symExpr`) must be aligned to the memory access."""
        pass


    def assignSymbolicExpressionToRegister(self, symExpr, reg):
        # type: (Self, SymbolicExpression, Register) -> None
        """Assigns a SymbolicExpression to a Register. **Be careful**, use this function only if you know what you are doing.
The symbolic expression (`symExpr`) must be aligned to the targeted size register. The register must be a parent register."""
        pass


    def buildSemantics(self, inst):
        # type: (Self, Instruction) -> EXCEPTION
        """Builds the instruction semantics. Returns `EXCEPTION.NO_FAULT` if the instruction is supported."""
        pass


    def clearCallbacks(self, ):
        # type: (Self) -> None
        """Clears recorded callbacks."""
        pass


    def clearModes(self, ):
        # type: (Self) -> None
        """Clears recorded modes."""
        pass


    def clearConcreteMemoryValue(self, addr_mem, size):
        # type: (Self, int | MemoryAccess, int) -> None
        """Clears concrete values assigned to the memory cells.

Clears concrete values assigned to the memory cells from `addr` to `addr + size`."""
        pass


    def clearPathConstraints(self, ):
        # type: (Self) -> None
        """Clears the current path predicate."""
        pass


    def concretizeAllMemory(self, ):
        # type: (Self) -> None
        """Concretizes all symbolic memory references."""
        pass


    def concretizeAllRegister(self, ):
        # type: (Self) -> None
        """Concretizes all symbolic register references."""
        pass


    def concretizeMemory(self, addr_mem):
        # type: (Self, int | MemoryAccess) -> None
        """Concretizes a specific symbolic memory reference.

Concretizes a specific symbolic memory reference."""
        pass


    def concretizeRegister(self, reg):
        # type: (Self, Register) -> None
        """Concretizes a specific symbolic register reference."""
        pass


    def createSymbolicMemoryExpression(self, inst, node, mem, comment):
        # type: (Self, Instruction, AstNode, MemoryAccess, str) -> SymbolicExpression
        """Returns the new symbolic memory expression and links this expression to the instruction."""
        pass


    def createSymbolicRegisterExpression(self, inst, node, reg, comment):
        # type: (Self, Instruction, AstNode, Register, str) -> SymbolicExpression
        """Returns the new symbolic register expression and links this expression to the instruction."""
        pass


    def createSymbolicVolatileExpression(self, inst, node, comment):
        # type: (Self, Instruction, AstNode, str) -> SymbolicExpression
        """Returns the new symbolic volatile expression and links this expression to the instruction."""
        pass


    def disassembly(self, addr_block_inst, count_addr=0):
        # type: (Self, int | BasicBlock | Instruction, int) -> None
        """Disassembles the instruction and sets up operands.

Disassembles a basic block with a potential given base address.

Disassembles a concrete memory area from `addr` and returns a list of at most `count` disassembled instructions.

Disassembles a concrete memory area from `addr` to control flow instruction and returns a BasicBlock."""
        pass


    def evaluateAstViaSolver(self, node):
        # type: (Self, AstNode) -> int
        """Evaluates an AST via the solver and returns the concrete value."""
        pass


    def getAllRegisters(self, ):
        # type: (Self) -> List[Register]
        """Returns the list of all registers. Each item of this list is a Register."""
        pass


    def getArchitecture(self, ):
        # type: (Self) -> ARCH
        """Returns the current architecture used."""
        pass


    def getAstContext(self, ):
        # type: (Self) -> AstContext
        """Returns the AST context to create and modify nodes."""
        pass


    def getAstRepresentationMode(self, ):
        # type: (Self) -> AST_REPRESENTATION
        """Returns the current AST representation mode."""
        pass


    def getConcreteMemoryAreaValue(self, addr, size, callbacks=True):
        # type: (Self, int, int, bool) -> bytes
        """Returns the concrete value of a memory area."""
        pass


    def getConcreteMemoryValue(self, addr_mem, callbacks=True):
        # type: (Self, int | MemoryAccess, bool) -> int
        """Returns the concrete value of a memory cell.

Returns the concrete value of memory cells."""
        pass


    def getConcreteRegisterValue(self, reg, callbacks=True):
        # type: (Self, Register, bool) -> int
        """Returns the concrete value of a register."""
        pass


    def getConcreteVariableValue(self, symVar):
        # type: (Self, SymbolicVariable) -> int
        """Returns the concrete value of a symbolic variable."""
        pass


    def getGprBitSize(self, ):
        # type: (Self) -> int
        """Returns the size in bits of the General Purpose Registers."""
        pass


    def getGprSize(self, ):
        # type: (Self) -> int
        """Returns the size in bytes of the General Purpose Registers."""
        pass


    def getImmediateAst(self, imm):
        # type: (Self, Immediate) -> AstNode
        """Returns the AST corresponding to the Immediate."""
        pass


    def getMemoryAst(self, mem):
        # type: (Self, MemoryAccess) -> AstNode
        """Returns the AST corresponding to the MemoryAccess with the SSA form."""
        pass


    def getModel(self, node, status=False, timeout=0):
        # type: (Self, AstNode, bool, int) -> dict
        """Computes and returns a model as a dictionary of {integer symVarId : SolverModel model} from a symbolic constraint.
If status is True, returns a tuple of (dict model, SOLVER_STATE status, integer solvingTime)."""
        pass


    def getModels(self, node, limit, status=False, timeout=0):
        # type: (Self, AstNode, int, bool, int) -> List[dict]
        """Computes and returns several models from a symbolic constraint. The `limit` is the number of models returned.
If status is True, returns a tuple of ([dict model, ...], SOLVER_STATE status, integer solvingTime)."""
        pass


    def getParentRegister(self, reg):
        # type: (Self, Register) -> Register
        """Returns the parent Register from a Register."""
        pass


    def getParentRegisters(self, ):
        # type: (Self) -> List[Register]
        """Returns the list of parent registers. Each item of this list is a Register."""
        pass


    def getPathConstraints(self, ):
        # type: (Self) -> List[PathConstraint]
        """Returns the logical conjunction vector of path constraints as a list of PathConstraint."""
        pass


    def getPathPredicate(self, ):
        # type: (Self) -> AstNode
        """Returns the current path predicate as an AST of logical conjunction of each taken branch."""
        pass


    def getPathPredicateSize(self, ):
        # type: (Self) -> int
        """Returns the size of the path predicate (number of constraints)."""
        pass


    def getPredicatesToReachAddress(self, addr):
        # type: (Self, int) -> List[AstNode]
        """Returns path predicates which may reach the targeted address."""
        pass


    def getRegister(self, id_name):
        # type: (Self, str | REG) -> Register
        """Returns the Register class corresponding to a REG id.

Returns the Register class corresponding to a string."""
        pass


    def getRegisterAst(self, reg):
        # type: (Self, Register) -> AstNode
        """Returns the AST corresponding to the Register with the SSA form."""
        pass


    def getSolver(self, ):
        # type: (Self) -> SOLVER
        """Returns the SMT solver engine currently used."""
        pass


    def getSymbolicExpression(self, symExprId):
        # type: (Self, int) -> SymbolicExpression
        """Returns the symbolic expression corresponding to an id."""
        pass


    def getSymbolicExpressions(self, ):
        # type: (Self) -> dict
        """Returns all symbolic expressions as a dictionary of {integer SymExprId : SymbolicExpression expr}."""
        pass


    def getSymbolicMemory(self, _addr):
        # type: (Self, int | None) -> dict
        """Returns the map of symbolic memory as {integer address : SymbolicExpression expr}.

Returns the SymbolicExpression corresponding to a memory address."""
        pass


    def getSymbolicMemoryValue(self, addr_mem):
        # type: (Self, int | MemoryAccess) -> int
        """Returns the symbolic memory value.

Returns the symbolic memory value."""
        pass


    def getSymbolicRegisters(self, ):
        # type: (Self) -> dict
        """Returns the map of symbolic registers as {REG reg : SymbolicExpression expr}."""
        pass


    def getSymbolicRegister(self, reg):
        # type: (Self, Register) -> SymbolicExpression
        """Returns the SymbolicExpression corresponding to the parent register."""
        pass


    def getSymbolicRegisterValue(self, reg):
        # type: (Self, Register) -> int
        """Returns the symbolic register value."""
        pass


    def getSymbolicVariable(self, symVarId_symVarName):
        # type: (Self, int | str) -> SymbolicVariable
        """Returns the symbolic variable corresponding to a symbolic variable id.

Returns the symbolic variable corresponding to a symbolic variable name."""
        pass


    def getSymbolicVariables(self, ):
        # type: (Self) -> dict
        """Returns all symbolic variables as a dictionary of {integer SymVarId : SymbolicVariable var}."""
        pass


    def getTaintedMemory(self, ):
        # type: (Self) -> List[int]
        """Returns the list of all tainted addresses."""
        pass


    def getTaintedRegisters(self, ):
        # type: (Self) -> List[Register]
        """Returns the list of all tainted registers."""
        pass


    def getTaintedSymbolicExpressions(self, ):
        # type: (Self) -> List[SymbolicExpression]
        """Returns the list of all tainted symbolic expressions."""
        pass


    def initLeaAst(self, mem):
        # type: (Self, MemoryAccess) -> None
        """Initializes the load effective address of a given memory access."""
        pass


    def isArchitectureValid(self, ):
        # type: (Self) -> bool
        """Returns true if the architecture is valid."""
        pass


    def isConcreteMemoryValueDefined(self, addr_mem, size):
        # type: (Self, int | MemoryAccess, int) -> bool
        """Returns true if memory cells have a defined concrete value.

Returns true if memory cells have a defined concrete value."""
        pass


    def isFlag(self, reg):
        # type: (Self, Register) -> bool
        """Returns true if the register is a flag."""
        pass


    def isMemorySymbolized(self, addr_mem):
        # type: (Self, int | MemoryAccess) -> bool
        """Returns true if the memory cell expression contains a symbolic variable.

Returns true if memory cell expressions contain symbolic variables."""
        pass


    def isMemoryTainted(self, addr_mem):
        # type: (Self, int | MemoryAccess) -> bool
        """Returns true if the address is tainted.

Returns true if the memory is tainted."""
        pass


    def isModeEnabled(self, mode):
        # type: (Self, MODE) -> bool
        """Returns true if the mode is enabled."""
        pass


    def isRegister(self, reg):
        # type: (Self, Register) -> bool
        """Returns true if the register is a register (see also isFlag())."""
        pass


    def isRegisterSymbolized(self, reg):
        # type: (Self, Register) -> bool
        """Returns true if the register expression contains a symbolic variable."""
        pass


    def isRegisterTainted(self, reg):
        # type: (Self, Register) -> bool
        """Returns true if the register is tainted."""
        pass


    def isRegisterValid(self, reg):
        # type: (Self, Register) -> bool
        """Returns true if the register is valid."""
        pass


    def isSat(self, node):
        # type: (Self, AstNode) -> bool
        """Returns true if an expression is satisfiable."""
        pass


    def isSymbolicExpressionExists(self, symExprId):
        # type: (Self, int) -> bool
        """Returns true if the symbolic expression id exists."""
        pass


    def isThumb(self, ):
        # type: (Self) -> bool
        """Returns true if execution mode is Thumb (only valid for ARM32)."""
        pass


    def liftToDot(self, node_expr):
        # type: (Self, AstNode | SymbolicExpression) -> str
        """Lifts an AST and all its references to Dot format.

Lifts a symbolic expression and all its references to Dot format."""
        pass


    def liftToLLVM(self, node_expr, fname="__triton", optimize=False):
        # type: (Self, AstNode | SymbolicExpression, str, bool) -> str
        """Lifts an AST node and all its references to LLVM IR. `fname` is the name of the LLVM function, by default it's `__triton`. If `optimize` is true, perform optimizations (-O3 -Oz).

Lifts a symbolic expression and all its references to LLVM IR. `fname` is the name of the LLVM function, by default it's `__triton`. If `optimize` is true, perform optimizations (-O3 -Oz)."""
        pass


    def liftToPython(self, expr, icomment=False):
        # type: (Self, SymbolicExpression, bool) -> str
        """Lifts a symbolic expression and all its references to Python format. If `icomment` is true, then print instructions assembly in expression comments."""
        pass


    def liftToSMT(self, expr, assert_=False, icomment=False):
        # type: (Self, SymbolicExpression, bool, bool) -> str
        """Lifts a symbolic expression and all its references to SMT format. If `assert_` is true, then (assert <expr>). If `icomment` is true, then print instructions assembly in expression comments."""
        pass


    def newSymbolicExpression(self, node, comment=""):
        # type: (Self, AstNode, str) -> SymbolicExpression
        """Returns a new symbolic expression. Note that if there are simplification passes recorded, simplifications will be applied."""
        pass


    def newSymbolicVariable(self, varSize, alias=""):
        # type: (Self, int, str) -> SymbolicVariable
        """Returns a new symbolic variable."""
        pass


    def popPathConstraint(self, ):
        # type: (Self) -> None
        """Pops the last constraints added to the path predicate."""
        pass


    def processing(self, block_inst, addr=0):
        # type: (Self, BasicBlock | Instruction, int) -> EXCEPTION
        """Processes an instruction and updates engines according to the instruction semantics. Returns `EXCEPTION.NO_FAULT` if the instruction is supported.

Processes a basic block with a potential given base address and updates engines according to the instructions semantics."""
        pass


    def pushPathConstraint(self, node, comment=""):
        # type: (Self, AstNode, str) -> None
        """Pushs constraints to the current path predicate."""
        pass


    def removeCallback(self, kind, cb):
        # type: (Self, CALLBACK, Callable) -> None
        """Removes a recorded callback."""
        pass


    def reset(self, ):
        # type: (Self) -> None
        """Resets everything."""
        pass


    def setArchitecture(self, arch):
        # type: (Self, ARCH) -> None
        """Initializes an architecture. This function must be called before any call to the rest of the API."""
        pass


    def setAstRepresentationMode(self, mode):
        # type: (Self, AST_REPRESENTATION) -> None
        """Sets the AST representation."""
        pass


    def setConcreteMemoryAreaValue(self, addr, args_opcodes, callbacks=True):
        # type: (Self, int, List[int] | bytes, bool) -> None
        """Sets the concrete value of a memory area. Note that setting a concrete value will probably imply a desynchronization with
the symbolic state (if it exists). You should probably use the concretize functions after this.

Sets the concrete value of a memory area. Note that setting a concrete value will probably imply a desynchronization with
the symbolic state (if it exists). You should probably use the concretize functions after this."""
        pass


    def setConcreteMemoryValue(self, addr_mem, value, callbacks=True):
        # type: (Self, int | MemoryAccess, int, bool) -> None
        """Sets the concrete value of a memory cell. Note that setting a concrete value will probably imply a desynchronization with
the symbolic state (if it exists). You should probably use the concretize functions after this.

Sets the concrete value of memory cells. Note that setting a concrete value will probably imply a desynchronization with
the symbolic state (if it exists). You should probably use the concretize functions after this."""
        pass


    def setConcreteRegisterValue(self, reg, value, callbacks=True):
        # type: (Self, Register, int, bool) -> None
        """Sets the concrete value of a register. Note that setting a concrete value will probably imply a desynchronization with
the symbolic state (if it exists). You should probably use the concretize functions after this."""
        pass


    def setConcreteVariableValue(self, symVar, value):
        # type: (Self, SymbolicVariable, int) -> None
        """Sets the concrete value of a symbolic variable."""
        pass


    def setMode(self, mode, flag):
        # type: (Self, MODE, bool) -> None
        """Enables or disables a specific mode."""
        pass


    def setSolver(self, solver):
        # type: (Self, SOLVER) -> None
        """Defines an SMT solver"""
        pass


    def setSolverMemoryLimit(self, megabytes):
        # type: (Self, int) -> None
        """Defines a solver memory consumption limit (in megabytes)"""
        pass


    def setSolverTimeout(self, ms):
        # type: (Self, int) -> None
        """Defines a solver timeout (in milliseconds)"""
        pass


    def setTaintMemory(self, mem, flag):
        # type: (Self, MemoryAccess, bool) -> bool
        """Sets the targeted memory as tainted or not. Returns true if the memory is still tainted."""
        pass


    def setTaintRegister(self, reg, flag):
        # type: (Self, Register, bool) -> bool
        """Sets the targeted register as tainted or not. Returns true if the register is still tainted."""
        pass


    def setThumb(self, state):
        # type: (Self, bool) -> None
        """Sets CPU state to Thumb mode (only valid for ARM32)."""
        pass


    def simplify(self, node_block, padding_solver=False, llvm=False):
        # type: (Self, BasicBlock | AstNode, bool, bool) -> AstNode
        """Calls all simplification callbacks recorded and returns a new simplified node. If the `solver` flag is
set to True, Triton will use the current solver instance to simplify the given `node`. If `llvm` is true,
we use LLVM to simplify node.

Performs a dead store elimination simplification on a given block. If `padding` is true, keep addresses aligned and padds with NOP instructions."""
        pass


    def sliceExpressions(self, expr):
        # type: (Self, SymbolicExpression) -> dict
        """Slices expressions from a given one (backward slicing) and returns all symbolic expressions as a dictionary of {integer SymExprId : SymbolicExpression expr}."""
        pass


    def symbolizeExpression(self, symExprId, symVarSize, symVarAlias=""):
        # type: (Self, int, int, str) -> SymbolicVariable
        """Converts a symbolic expression to a symbolic variable. `symVarSize` must be in bits. This function returns the new symbolic variable created."""
        pass


    def symbolizeMemory(self, mem, symVarAlias=""):
        # type: (Self, MemoryAccess, str) -> SymbolicVariable
        """Converts a symbolic memory expression to a symbolic variable. This function returns the new symbolic variable created."""
        pass


    def symbolizeRegister(self, reg, symVarAlias=""):
        # type: (Self, Register, str) -> SymbolicVariable
        """Converts a symbolic register expression to a symbolic variable. This function returns the new symbolic variable created."""
        pass


    def synthesize(self, node, constant=True, subexpr=True, opaque=False):
        # type: (Self, AstNode, bool, bool, bool) -> AstNode
        """Synthesizes a given node. If `constant` is defined to True, performs a constant synthesis. If `opaque` is true, perform opaque constant synthesis. If `subexpr` is defined to True, performs synthesis on sub-expressions."""
        pass


    def taintAssignment(self, regDst_memDst, regSrc_memSrc_immSrc):
        # type: (Self, Register | MemoryAccess, MemoryAccess | Immediate | Register) -> bool
        """Taints `memDst` from `immSrc` with an assignment - `memDst` is untained. Returns true if the `memDst` is still tainted.

Taints `memDst` from `memSrc` with an assignment - `memDst` is tainted if `memSrc` is tainted, otherwise
`memDst` is untained. Returns true if `memDst` is tainted.

Taints `memDst` from `regSrc` with an assignment - `memDst` is tainted if `regSrc` is tainted, otherwise
`memDst` is untained. Return true if `memDst` is tainted.

Taints `regDst` from `immSrc` with an assignment - `regDst` is untained. Returns true if `reDst` is still tainted.

Taints `regDst` from `MemSrc` with an assignment - `regDst` is tainted if `memSrc` is tainted, otherwise
`regDst` is untained. Return true if `regDst` is tainted.

Taints `regDst` from `regSrc` with an assignment - `regDst` is tainted if `regSrc` is tainted, otherwise
`regDst` is untained. Return true if `regDst` is tainted."""
        pass


    def taintMemory(self, addr_mem):
        # type: (Self, int | MemoryAccess) -> bool
        """Taints an address. Returns true if the address is tainted.

Taints a memory. Returns true if the memory is tainted."""
        pass


    def taintRegister(self, reg):
        # type: (Self, Register) -> bool
        """Taints a register. Returns true if the register is tainted."""
        pass


    def taintUnion(self, regDst_memDst, regSrc_memSrc_immSrc):
        # type: (Self, Register | MemoryAccess, MemoryAccess | Immediate | Register) -> bool
        """Taints `memDst` from `immSrc` with an union - `memDst` does not changes. Returns true if `memDst` is tainted.

Taints `memDst` from `memSrc` with an union - `memDst` is tainted if `memDst` or `memSrc` are
tainted. Returns true if `memDst` is tainted.

Taints `memDst` from `RegSrc` with an union - `memDst` is tainted if `memDst` or `regSrc` are
tainted. Returns true if `memDst` is tainted.

Taints `regDst` from `immSrc` with an union - `regDst` does not changes. Returns true if `regDst` is tainted.

Taints `regDst` from `memSrc` with an union - `regDst` is tainted if `regDst` or `memSrc` are
tainted. Returns true if `regDst` is tainted.

Taints `regDst` from `regSrc` with an union - `regDst` is tainted if `regDst` or `regSrc` are
tainted. Returns true if `regDst` is tainted."""
        pass


    def untaintMemory(self, addr_mem):
        # type: (Self, int | MemoryAccess) -> bool
        """Untaints an address. Returns true if the address is still tainted.

Untaints a memory. Returns true if the memory is still tainted."""
        pass


    def untaintRegister(self, reg):
        # type: (Self, Register) -> bool
        """Untaints a register. Returns true if the register is still tainted."""
        pass




class Immediate:
    def __init__(self, *args, **kargs):
        pass


    def getBitSize(self, ):
        # type: (Self) -> int
        """Returns the size (in bits) of the immediate.<br>
e.g: `64`"""
        pass


    def getBitvector(self, ):
        # type: (Self) -> BitsVector
        """Returns the bit vector."""
        pass


    def getShiftType(self, ):
        # type: (Self) -> SHIFT
        """Returns the shift type of the operand. Mainly used for AArch64.<br>
e.g: `SHIFT.ARM.LSL`"""
        pass


    def getShiftImmediate(self, ):
        # type: (Self) -> int
        """Returns the shift immediate value of the operand. Mainly used for AArch64 and ARM32.<br>
e.g: `2`"""
        pass


    def getShiftRegister(self, ):
        # type: (Self) -> REG
        """Returns the shift register of the operand. Mainly used for ARM32.<br>
e.g: `REG.ARM32.R0`"""
        pass


    def getSize(self, ):
        # type: (Self) -> int
        """Returns the size (in bytes) of the immediate.<br>
e.g: `8`"""
        pass


    def getType(self, ):
        # type: (Self) -> OPERAND
        """Returns the type of the immediate. In this case this function returns `OPERAND.IMM`."""
        pass


    def getValue(self, ):
        # type: (Self) -> int
        """Returns the immediate value."""
        pass


    def setValue(self, value, size):
        # type: (Self, int, int) -> None
        """Sets the immediate value."""
        pass




class MemoryAccess:
    def __init__(self, *args, **kargs):
        pass


    def getAddress(self, ):
        # type: (Self) -> int
        """Returns the target address of the memory access.<br>
e.g: `0x7fffdd745ae0`"""
        pass


    def getBaseRegister(self, ):
        # type: (Self) -> Register
        """Returns the base register (if exists) of the memory access.<br>"""
        pass


    def getBitSize(self, ):
        # type: (Self) -> int
        """Returns the size (in bits) of the memory access.<br>
e.g: `64`"""
        pass


    def getBitvector(self, ):
        # type: (Self) -> BitsVector
        """Returns the bit vector of the memory cells."""
        pass


    def getDisplacement(self, ):
        # type: (Self) -> Immediate
        """Returns the displacement (if exists) of the memory access."""
        pass


    def getIndexRegister(self, ):
        # type: (Self) -> Register
        """Returns the index register (if exists) of the memory access.<br>"""
        pass


    def getLeaAst(self, ):
        # type: (Self) -> AstNode
        """Returns the AST of the memory access (LEA)."""
        pass


    def getScale(self, ):
        # type: (Self) -> Immediate
        """Returns the scale (if exists) of the memory access."""
        pass


    def getSegmentRegister(self, ):
        # type: (Self) -> Register
        """Returns the segment register (if exists) of the memory access. Note that to be user-friendly, the
segment register is used as base register and not as a selector into the GDT.<br>"""
        pass


    def getSize(self, ):
        # type: (Self) -> int
        """Returns the size (in bytes) of the memory access.<br>
e.g: `8`"""
        pass


    def getType(self, ):
        # type: (Self) -> OPERAND
        """Returns the type of the memory access. In this case this function returns `OPERAND.MEM`."""
        pass


    def isOverlapWith(self, other):
        # type: (Self, MemoryAccess) -> bool
        """Returns true if `other` and `self` overlap."""
        pass


    def setBaseRegister(self, reg):
        # type: (Self, Register) -> None
        """Sets the base register of the memory access."""
        pass


    def setDisplacement(self, imm):
        # type: (Self, Immediate) -> None
        """Sets the displacement of the memory access."""
        pass


    def setIndexRegister(self, reg):
        # type: (Self, Register) -> None
        """Sets the index register of the memory access."""
        pass


    def setScale(self, imm):
        # type: (Self, Immediate) -> None
        """Sets the scale of the memory access."""
        pass




class SolverModel:
    def __init__(self, *args, **kargs):
        pass


    def getId(self, ):
        # type: (Self) -> int
        """Returns the id of the model. This id is the same as the variable id."""
        pass


    def getValue(self, ):
        # type: (Self) -> int
        """Returns the value of the model."""
        pass


    def getVariable(self, ):
        # type: (Self) -> SymbolicVariable
        """Returns the symbolic variable."""
        pass




class Instruction:
    def __init__(self, *args, **kargs):
        pass


    def getAddress(self, ):
        # type: (Self) -> int
        """Returns the address of the instruction."""
        pass


    def getCodeCondition(self, ):
        # type: (Self) -> int
        """Returns the code condition of the instruction (mainly used for AArch64)."""
        pass


    def getDisassembly(self, ):
        # type: (Self) -> str
        """Returns the disassembly of the instruction."""
        pass


    def getLoadAccess(self, ):
        # type: (Self) -> List[Tuple]
        """Returns the list of all implicit and explicit LOAD accesses as a list of tuple <MemoryAccess, AstNode>."""
        pass


    def getNextAddress(self, ):
        # type: (Self) -> int
        """Returns the next address of the instruction."""
        pass


    def getOpcode(self, ):
        # type: (Self) -> bytes
        """Returns the opcode of the instruction."""
        pass


    def getOperands(self, ):
        # type: (Self) -> List[Union[Immediate, MemoryAccess, Register]]
        """Returns the operands of the instruction as a list of Immediate, MemoryAccess or Register."""
        pass


    def getPrefix(self, ):
        # type: (Self) -> PREFIX
        """Returns the instruction prefix. Mainly used for X86."""
        pass


    def getReadImmediates(self, ):
        # type: (Self) -> List[Tuple]
        """Returns a list of tuple <Immediate, AstNode> which represents all implicit and explicit immediate inputs."""
        pass


    def getReadRegisters(self, ):
        # type: (Self) -> List[Tuple]
        """Returns a list of tuple <Register, AstNode> which represents all implicit and explicit register (flags includes) inputs."""
        pass


    def getSize(self, ):
        # type: (Self) -> int
        """Returns the size of the instruction."""
        pass


    def getStoreAccess(self, ):
        # type: (Self) -> List[Tuple]
        """Returns the list of all implicit and explicit STORE accesses as a list of tuple <MemoryAccess, AstNode>."""
        pass


    def getSymbolicExpressions(self, ):
        # type: (Self) -> List[SymbolicExpression]
        """Returns the list of symbolic expressions of the instruction."""
        pass


    def getThreadId(self, ):
        # type: (Self) -> int
        """Returns the thread id of the instruction."""
        pass


    def getType(self, ):
        # type: (Self) -> OPCODE
        """Returns the type of the instruction."""
        pass


    def getUndefinedRegisters(self, ):
        # type: (Self) -> List[Register]
        """Returns a list Register which represents all implicit and explicit undefined registers."""
        pass


    def getWrittenRegisters(self, ):
        # type: (Self) -> List[Tuple]
        """Returns a list of tuples <Register, AstNode> which represents all implicit and explicit register (flags includes) outputs."""
        pass


    def isBranch(self, ):
        # type: (Self) -> bool
        """Returns true if the instruction is a branch (i.e x86: JUMP, JCC)."""
        pass


    def isConditionTaken(self, ):
        # type: (Self) -> bool
        """Returns true if the condition is taken (i.e x86: JCC, CMOVCC, SETCC, ...)."""
        pass


    def isControlFlow(self, ):
        # type: (Self) -> bool
        """Returns true if the instruction modifies the control flow (i.e x86: JUMP, JCC, CALL, RET)."""
        pass


    def isMemoryRead(self, ):
        # type: (Self) -> bool
        """Returns true if the instruction contains an expression which reads the memory."""
        pass


    def isMemoryWrite(self, ):
        # type: (Self) -> bool
        """Returns true if the instruction contains an expression which writes into the memory."""
        pass


    def isPrefixed(self, ):
        # type: (Self) -> bool
        """Returns true if the instruction has a prefix."""
        pass


    def isSymbolized(self, ):
        # type: (Self) -> bool
        """Returns true if at least one of its SymbolicExpression contains a symbolic variable."""
        pass


    def isTainted(self, ):
        # type: (Self) -> bool
        """Returns true if at least one of its SymbolicExpression is tainted."""
        pass


    def isWriteBack(self, ):
        # type: (Self) -> bool
        """Returns true if the instruction performs a write back. Mainly used for AArch64 instructions like LDR."""
        pass


    def isUpdateFlag(self, ):
        # type: (Self) -> bool
        """Returns true if the instruction updates flags. Mainly used for AArch64 instructions like ADDS."""
        pass


    def isThumb(self, ):
        # type: (Self) -> bool
        """Returns true if the instruction is a Thumb instruction."""
        pass


    def setAddress(self, addr):
        # type: (Self, int) -> None
        """Sets the address of the instruction."""
        pass


    def setOpcode(self, opcode):
        # type: (Self, bytes) -> None
        """Sets the opcode of the instruction."""
        pass


    def setThreadId(self, tid):
        # type: (Self, int) -> None
        """Sets the thread id of the instruction."""
        pass




class BitsVector:
    def __init__(self, *args, **kargs):
        pass


    def getHigh(self, ):
        # type: (Self) -> int
        """Returns the highest bit position."""
        pass


    def getLow(self, ):
        # type: (Self) -> int
        """Returns the lowest bit position."""
        pass


    def getMaxValue(self, ):
        # type: (Self) -> int
        """Returns the max value of the vector."""
        pass


    def getVectorSize(self, ):
        # type: (Self) -> int
        """Returns the size of the vector."""
        pass




class SymbolicExpression:
    def __init__(self, *args, **kargs):
        pass


    def getAst(self, ):
        # type: (Self) -> AstNode
        """Returns the AST root node of the symbolic expression."""
        pass


    def getComment(self, ):
        # type: (Self) -> str
        """Returns the comment (if exists) of the symbolic expression."""
        pass


    def getDisassembly(self, ):
        # type: (Self) -> str
        """Returns the instruction disassembly where the symbolic expression comes from."""
        pass


    def getId(self, ):
        # type: (Self) -> int
        """Returns the id of the symbolic expression. This id is always unique.<br>
e.g: `2387`"""
        pass


    def getNewAst(self, ):
        # type: (Self) -> AstNode
        """Returns a new AST root node of the symbolic expression. This new instance is a duplicate of the original node and may be changed without changing the original semantics."""
        pass


    def getOrigin(self, ):
        # type: (Self) -> Register
        """Returns the origin of the symbolic expression. For example, if the symbolic expression is assigned to a memory cell, this function returns
a MemoryAccess, else if it is assigned to a register, this function returns a Register otherwise it returns None. Note that
for a MemoryAccess all information about LEA are lost at this level."""
        pass


    def getType(self, ):
        # type: (Self) -> SYMBOLIC
        """Returns the type of the symbolic expression.<br>
e.g: `SYMBOLIC.REGISTER_EXPRESSION`"""
        pass


    def isMemory(self, ):
        # type: (Self) -> bool
        """Returns true if the expression is assigned to memory."""
        pass


    def isRegister(self, ):
        # type: (Self) -> bool
        """Returns true if the expression is assigned to a register."""
        pass


    def isSymbolized(self, ):
        # type: (Self) -> bool
        """Returns true if the expression contains a symbolic variable."""
        pass


    def isTainted(self, ):
        # type: (Self) -> bool
        """Returns true if the expression is tainted."""
        pass


    def setAst(self, node):
        # type: (Self, AstNode) -> None
        """Sets a root node."""
        pass


    def setComment(self, comment):
        # type: (Self, str) -> None
        """Sets a comment to the symbolic expression."""
        pass



class SYMBOLIC(IntEnum):
    MEMORY_EXPRESSION = 1
    MEMORY_VARIABLE = 2
    REGISTER_EXPRESSION = 3
    REGISTER_VARIABLE = 4
    UNDEFINED_VARIABLE = 5
    VOLATILE_EXPRESSION = 6

class SHIFT(IntEnum):
    pass
    class ARM(IntEnum):
        INVALID = 1
        ASR = 2
        LSL = 3
        LSR = 4
        ROR = 5
        RRX = 6
        ASR_REG = 7
        LSL_REG = 8
        LSR_REG = 9
        ROR_REG = 10
        RRX_REG = 11

class CALLBACK(IntEnum):
    GET_CONCRETE_MEMORY_VALUE = 1
    GET_CONCRETE_REGISTER_VALUE = 2
    SET_CONCRETE_MEMORY_VALUE = 3
    SET_CONCRETE_REGISTER_VALUE = 4
    SYMBOLIC_SIMPLIFICATION = 5

class SOLVER_STATE(IntEnum):
    OUTOFMEM = 1
    SAT = 2
    TIMEOUT = 3
    UNKNOWN = 4
    UNSAT = 5

class EXCEPTION(IntEnum):
    NO_FAULT = 1
    FAULT_DE = 2
    FAULT_BP = 3
    FAULT_UD = 4
    FAULT_GP = 5

class SOLVER(IntEnum):
    pass

class CONDITION(IntEnum):
    pass
    class ARM(IntEnum):
        INVALID = 1
        AL = 2
        EQ = 3
        GE = 4
        GT = 5
        HI = 6
        HS = 7
        LE = 8
        LO = 9
        LS = 10
        LT = 11
        MI = 12
        NE = 13
        PL = 14
        VC = 15
        VS = 16

class STUBS(IntEnum):
    pass
    class AARCH64(IntEnum):
        pass
        class LIBC(IntEnum):
            code = 1
            symbols = 2
    class I386(IntEnum):
        pass
        class SYSTEMV(IntEnum):
            pass
            class LIBC(IntEnum):
                code = 3
                symbols = 4
    class X8664(IntEnum):
        pass
        class MS(IntEnum):
            pass
            class LIBC(IntEnum):
                code = 5
                symbols = 6
        class SYSTEMV(IntEnum):
            pass
            class LIBC(IntEnum):
                code = 7
                symbols = 8

class OPERAND(IntEnum):
    INVALID = 1
    IMM = 2
    MEM = 3
    REG = 4

class VAS(IntEnum):
    pass
    class ARM(IntEnum):
        INVALID = 1
        v16B = 2
        v8B = 3
        v8H = 4
        v4H = 5
        v4S = 6
        v2S = 7
        v2D = 8
        v1D = 9

class PREFIX(IntEnum):
    pass
    class X86(IntEnum):
        INVALID = 1
        LOCK = 2
        REP = 3
        REPE = 4
        REPNE = 5


class AARCH64_class:

    X0 = 0
    X1 = 1
    X2 = 2
    X3 = 3
    X4 = 4
    X5 = 5
    X6 = 6
    X7 = 7
    X8 = 8
    X9 = 9
    X10 = 10
    X11 = 11
    X12 = 12
    X13 = 13
    X14 = 14
    X15 = 15
    X16 = 16
    X17 = 17
    X18 = 18
    X19 = 19
    X20 = 20
    X21 = 21
    X22 = 22
    X23 = 23
    X24 = 24
    X25 = 25
    X26 = 26
    X27 = 27
    X28 = 28
    X29 = 29
    X30 = 30
    W0 = 31
    W1 = 32
    W2 = 33
    W3 = 34
    W4 = 35
    W5 = 36
    W6 = 37
    W7 = 38
    W8 = 39
    W9 = 40
    W10 = 41
    W11 = 42
    W12 = 43
    W13 = 44
    W14 = 45
    W15 = 46
    W16 = 47
    W17 = 48
    W18 = 49
    W19 = 50
    W20 = 51
    W21 = 52
    W22 = 53
    W23 = 54
    W24 = 55
    W25 = 56
    W26 = 57
    W27 = 58
    W28 = 59
    W29 = 60
    W30 = 61
    SPSR = 62
    SP = 63
    WSP = 64
    PC = 65
    XZR = 66
    WZR = 67
    C = 68
    N = 69
    V = 70
    Z = 71
    Q0 = 72
    Q1 = 73
    Q2 = 74
    Q3 = 75
    Q4 = 76
    Q5 = 77
    Q6 = 78
    Q7 = 79
    Q8 = 80
    Q9 = 81
    Q10 = 82
    Q11 = 83
    Q12 = 84
    Q13 = 85
    Q14 = 86
    Q15 = 87
    Q16 = 88
    Q17 = 89
    Q18 = 90
    Q19 = 91
    Q20 = 92
    Q21 = 93
    Q22 = 94
    Q23 = 95
    Q24 = 96
    Q25 = 97
    Q26 = 98
    Q27 = 99
    Q28 = 100
    Q29 = 101
    Q30 = 102
    Q31 = 103
    D0 = 104
    D1 = 105
    D2 = 106
    D3 = 107
    D4 = 108
    D5 = 109
    D6 = 110
    D7 = 111
    D8 = 112
    D9 = 113
    D10 = 114
    D11 = 115
    D12 = 116
    D13 = 117
    D14 = 118
    D15 = 119
    D16 = 120
    D17 = 121
    D18 = 122
    D19 = 123
    D20 = 124
    D21 = 125
    D22 = 126
    D23 = 127
    D24 = 128
    D25 = 129
    D26 = 130
    D27 = 131
    D28 = 132
    D29 = 133
    D30 = 134
    D31 = 135
    S0 = 136
    S1 = 137
    S2 = 138
    S3 = 139
    S4 = 140
    S5 = 141
    S6 = 142
    S7 = 143
    S8 = 144
    S9 = 145
    S10 = 146
    S11 = 147
    S12 = 148
    S13 = 149
    S14 = 150
    S15 = 151
    S16 = 152
    S17 = 153
    S18 = 154
    S19 = 155
    S20 = 156
    S21 = 157
    S22 = 158
    S23 = 159
    S24 = 160
    S25 = 161
    S26 = 162
    S27 = 163
    S28 = 164
    S29 = 165
    S30 = 166
    S31 = 167
    H0 = 168
    H1 = 169
    H2 = 170
    H3 = 171
    H4 = 172
    H5 = 173
    H6 = 174
    H7 = 175
    H8 = 176
    H9 = 177
    H10 = 178
    H11 = 179
    H12 = 180
    H13 = 181
    H14 = 182
    H15 = 183
    H16 = 184
    H17 = 185
    H18 = 186
    H19 = 187
    H20 = 188
    H21 = 189
    H22 = 190
    H23 = 191
    H24 = 192
    H25 = 193
    H26 = 194
    H27 = 195
    H28 = 196
    H29 = 197
    H30 = 198
    H31 = 199
    B0 = 200
    B1 = 201
    B2 = 202
    B3 = 203
    B4 = 204
    B5 = 205
    B6 = 206
    B7 = 207
    B8 = 208
    B9 = 209
    B10 = 210
    B11 = 211
    B12 = 212
    B13 = 213
    B14 = 214
    B15 = 215
    B16 = 216
    B17 = 217
    B18 = 218
    B19 = 219
    B20 = 220
    B21 = 221
    B22 = 222
    B23 = 223
    B24 = 224
    B25 = 225
    B26 = 226
    B27 = 227
    B28 = 228
    B29 = 229
    B30 = 230
    B31 = 231
    V0 = 232
    V1 = 233
    V2 = 234
    V3 = 235
    V4 = 236
    V5 = 237
    V6 = 238
    V7 = 239
    V8 = 240
    V9 = 241
    V10 = 242
    V11 = 243
    V12 = 244
    V13 = 245
    V14 = 246
    V15 = 247
    V16 = 248
    V17 = 249
    V18 = 250
    V19 = 251
    V20 = 252
    V21 = 253
    V22 = 254
    V23 = 255
    V24 = 256
    V25 = 257
    V26 = 258
    V27 = 259
    V28 = 260
    V29 = 261
    V30 = 262
    V31 = 263
    ACTLR_EL1 = 264
    ACTLR_EL2 = 265
    ACTLR_EL3 = 266
    AFSR0_EL1 = 267
    AFSR0_EL12 = 268
    AFSR0_EL2 = 269
    AFSR0_EL3 = 270
    AFSR1_EL1 = 271
    AFSR1_EL12 = 272
    AFSR1_EL2 = 273
    AFSR1_EL3 = 274
    AIDR_EL1 = 275
    AMAIR_EL1 = 276
    AMAIR_EL12 = 277
    AMAIR_EL2 = 278
    AMAIR_EL3 = 279
    AMCFGR_EL0 = 280
    AMCGCR_EL0 = 281
    AMCNTENCLR0_EL0 = 282
    AMCNTENCLR1_EL0 = 283
    AMCNTENSET0_EL0 = 284
    AMCNTENSET1_EL0 = 285
    AMCR_EL0 = 286
    AMEVCNTR00_EL0 = 287
    AMEVCNTR01_EL0 = 288
    AMEVCNTR02_EL0 = 289
    AMEVCNTR03_EL0 = 290
    AMEVCNTR10_EL0 = 291
    AMEVCNTR110_EL0 = 292
    AMEVCNTR111_EL0 = 293
    AMEVCNTR112_EL0 = 294
    AMEVCNTR113_EL0 = 295
    AMEVCNTR114_EL0 = 296
    AMEVCNTR115_EL0 = 297
    AMEVCNTR11_EL0 = 298
    AMEVCNTR12_EL0 = 299
    AMEVCNTR13_EL0 = 300
    AMEVCNTR14_EL0 = 301
    AMEVCNTR15_EL0 = 302
    AMEVCNTR16_EL0 = 303
    AMEVCNTR17_EL0 = 304
    AMEVCNTR18_EL0 = 305
    AMEVCNTR19_EL0 = 306
    AMEVTYPER00_EL0 = 307
    AMEVTYPER01_EL0 = 308
    AMEVTYPER02_EL0 = 309
    AMEVTYPER03_EL0 = 310
    AMEVTYPER10_EL0 = 311
    AMEVTYPER110_EL0 = 312
    AMEVTYPER111_EL0 = 313
    AMEVTYPER112_EL0 = 314
    AMEVTYPER113_EL0 = 315
    AMEVTYPER114_EL0 = 316
    AMEVTYPER115_EL0 = 317
    AMEVTYPER11_EL0 = 318
    AMEVTYPER12_EL0 = 319
    AMEVTYPER13_EL0 = 320
    AMEVTYPER14_EL0 = 321
    AMEVTYPER15_EL0 = 322
    AMEVTYPER16_EL0 = 323
    AMEVTYPER17_EL0 = 324
    AMEVTYPER18_EL0 = 325
    AMEVTYPER19_EL0 = 326
    AMUSERENR_EL0 = 327
    APDAKEYHI_EL1 = 328
    APDAKEYLO_EL1 = 329
    APDBKEYHI_EL1 = 330
    APDBKEYLO_EL1 = 331
    APGAKEYHI_EL1 = 332
    APGAKEYLO_EL1 = 333
    APIAKEYHI_EL1 = 334
    APIAKEYLO_EL1 = 335
    APIBKEYHI_EL1 = 336
    APIBKEYLO_EL1 = 337
    CCSIDR2_EL1 = 338
    CCSIDR_EL1 = 339
    CLIDR_EL1 = 340
    CNTFRQ_EL0 = 341
    CNTHCTL_EL2 = 342
    CNTHPS_CTL_EL2 = 343
    CNTHPS_CVAL_EL2 = 344
    CNTHPS_TVAL_EL2 = 345
    CNTHP_CTL_EL2 = 346
    CNTHP_CVAL_EL2 = 347
    CNTHP_TVAL_EL2 = 348
    CNTHVS_CTL_EL2 = 349
    CNTHVS_CVAL_EL2 = 350
    CNTHVS_TVAL_EL2 = 351
    CNTHV_CTL_EL2 = 352
    CNTHV_CVAL_EL2 = 353
    CNTHV_TVAL_EL2 = 354
    CNTKCTL_EL1 = 355
    CNTKCTL_EL12 = 356
    CNTPCT_EL0 = 357
    CNTPS_CTL_EL1 = 358
    CNTPS_CVAL_EL1 = 359
    CNTPS_TVAL_EL1 = 360
    CNTP_CTL_EL0 = 361
    CNTP_CTL_EL02 = 362
    CNTP_CVAL_EL0 = 363
    CNTP_CVAL_EL02 = 364
    CNTP_TVAL_EL0 = 365
    CNTP_TVAL_EL02 = 366
    CNTVCT_EL0 = 367
    CNTVOFF_EL2 = 368
    CNTV_CTL_EL0 = 369
    CNTV_CTL_EL02 = 370
    CNTV_CVAL_EL0 = 371
    CNTV_CVAL_EL02 = 372
    CNTV_TVAL_EL0 = 373
    CNTV_TVAL_EL02 = 374
    CONTEXTIDR_EL1 = 375
    CONTEXTIDR_EL12 = 376
    CONTEXTIDR_EL2 = 377
    CPACR_EL1 = 378
    CPACR_EL12 = 379
    CPM_IOACC_CTL_EL3 = 380
    CPTR_EL2 = 381
    CPTR_EL3 = 382
    CSSELR_EL1 = 383
    CTR_EL0 = 384
    CURRENTEL = 385
    DACR32_EL2 = 386
    DAIF = 387
    DBGAUTHSTATUS_EL1 = 388
    DBGBCR0_EL1 = 389
    DBGBCR10_EL1 = 390
    DBGBCR11_EL1 = 391
    DBGBCR12_EL1 = 392
    DBGBCR13_EL1 = 393
    DBGBCR14_EL1 = 394
    DBGBCR15_EL1 = 395
    DBGBCR1_EL1 = 396
    DBGBCR2_EL1 = 397
    DBGBCR3_EL1 = 398
    DBGBCR4_EL1 = 399
    DBGBCR5_EL1 = 400
    DBGBCR6_EL1 = 401
    DBGBCR7_EL1 = 402
    DBGBCR8_EL1 = 403
    DBGBCR9_EL1 = 404
    DBGBVR0_EL1 = 405
    DBGBVR10_EL1 = 406
    DBGBVR11_EL1 = 407
    DBGBVR12_EL1 = 408
    DBGBVR13_EL1 = 409
    DBGBVR14_EL1 = 410
    DBGBVR15_EL1 = 411
    DBGBVR1_EL1 = 412
    DBGBVR2_EL1 = 413
    DBGBVR3_EL1 = 414
    DBGBVR4_EL1 = 415
    DBGBVR5_EL1 = 416
    DBGBVR6_EL1 = 417
    DBGBVR7_EL1 = 418
    DBGBVR8_EL1 = 419
    DBGBVR9_EL1 = 420
    DBGCLAIMCLR_EL1 = 421
    DBGCLAIMSET_EL1 = 422
    DBGDTRRX_EL0 = 423
    DBGDTR_EL0 = 424
    DBGPRCR_EL1 = 425
    DBGVCR32_EL2 = 426
    DBGWCR0_EL1 = 427
    DBGWCR10_EL1 = 428
    DBGWCR11_EL1 = 429
    DBGWCR12_EL1 = 430
    DBGWCR13_EL1 = 431
    DBGWCR14_EL1 = 432
    DBGWCR15_EL1 = 433
    DBGWCR1_EL1 = 434
    DBGWCR2_EL1 = 435
    DBGWCR3_EL1 = 436
    DBGWCR4_EL1 = 437
    DBGWCR5_EL1 = 438
    DBGWCR6_EL1 = 439
    DBGWCR7_EL1 = 440
    DBGWCR8_EL1 = 441
    DBGWCR9_EL1 = 442
    DBGWVR0_EL1 = 443
    DBGWVR10_EL1 = 444
    DBGWVR11_EL1 = 445
    DBGWVR12_EL1 = 446
    DBGWVR13_EL1 = 447
    DBGWVR14_EL1 = 448
    DBGWVR15_EL1 = 449
    DBGWVR1_EL1 = 450
    DBGWVR2_EL1 = 451
    DBGWVR3_EL1 = 452
    DBGWVR4_EL1 = 453
    DBGWVR5_EL1 = 454
    DBGWVR6_EL1 = 455
    DBGWVR7_EL1 = 456
    DBGWVR8_EL1 = 457
    DBGWVR9_EL1 = 458
    DCZID_EL0 = 459
    DISR_EL1 = 460
    DIT = 461
    DLR_EL0 = 462
    DSPSR_EL0 = 463
    ELR_EL1 = 464
    ELR_EL12 = 465
    ELR_EL2 = 466
    ELR_EL3 = 467
    ERRIDR_EL1 = 468
    ERRSELR_EL1 = 469
    ERXADDR_EL1 = 470
    ERXCTLR_EL1 = 471
    ERXFR_EL1 = 472
    ERXMISC0_EL1 = 473
    ERXMISC1_EL1 = 474
    ERXMISC2_EL1 = 475
    ERXMISC3_EL1 = 476
    ERXPFGCDN_EL1 = 477
    ERXPFGCTL_EL1 = 478
    ERXPFGF_EL1 = 479
    ERXSTATUS_EL1 = 480
    ESR_EL1 = 481
    ESR_EL12 = 482
    ESR_EL2 = 483
    ESR_EL3 = 484
    FAR_EL1 = 485
    FAR_EL12 = 486
    FAR_EL2 = 487
    FAR_EL3 = 488
    FPCR = 489
    FPEXC32_EL2 = 490
    FPSR = 491
    HACR_EL2 = 492
    HCR_EL2 = 493
    HPFAR_EL2 = 494
    HSTR_EL2 = 495
    ICC_AP0R0_EL1 = 496
    ICC_AP0R1_EL1 = 497
    ICC_AP0R2_EL1 = 498
    ICC_AP0R3_EL1 = 499
    ICC_AP1R0_EL1 = 500
    ICC_AP1R1_EL1 = 501
    ICC_AP1R2_EL1 = 502
    ICC_AP1R3_EL1 = 503
    ICC_ASGI1R_EL1 = 504
    ICC_BPR0_EL1 = 505
    ICC_BPR1_EL1 = 506
    ICC_CTLR_EL1 = 507
    ICC_CTLR_EL3 = 508
    ICC_DIR_EL1 = 509
    ICC_EOIR0_EL1 = 510
    ICC_EOIR1_EL1 = 511
    ICC_HPPIR0_EL1 = 512
    ICC_HPPIR1_EL1 = 513
    ICC_IAR0_EL1 = 514
    ICC_IAR1_EL1 = 515
    ICC_IGRPEN0_EL1 = 516
    ICC_IGRPEN1_EL1 = 517
    ICC_IGRPEN1_EL3 = 518
    ICC_PMR_EL1 = 519
    ICC_RPR_EL1 = 520
    ICC_SGI0R_EL1 = 521
    ICC_SGI1R_EL1 = 522
    ICC_SRE_EL1 = 523
    ICC_SRE_EL2 = 524
    ICC_SRE_EL3 = 525
    ICH_AP0R0_EL2 = 526
    ICH_AP0R1_EL2 = 527
    ICH_AP0R2_EL2 = 528
    ICH_AP0R3_EL2 = 529
    ICH_AP1R0_EL2 = 530
    ICH_AP1R1_EL2 = 531
    ICH_AP1R2_EL2 = 532
    ICH_AP1R3_EL2 = 533
    ICH_EISR_EL2 = 534
    ICH_ELRSR_EL2 = 535
    ICH_HCR_EL2 = 536
    ICH_LR0_EL2 = 537
    ICH_LR10_EL2 = 538
    ICH_LR11_EL2 = 539
    ICH_LR12_EL2 = 540
    ICH_LR13_EL2 = 541
    ICH_LR14_EL2 = 542
    ICH_LR15_EL2 = 543
    ICH_LR1_EL2 = 544
    ICH_LR2_EL2 = 545
    ICH_LR3_EL2 = 546
    ICH_LR4_EL2 = 547
    ICH_LR5_EL2 = 548
    ICH_LR6_EL2 = 549
    ICH_LR7_EL2 = 550
    ICH_LR8_EL2 = 551
    ICH_LR9_EL2 = 552
    ICH_MISR_EL2 = 553
    ICH_VMCR_EL2 = 554
    ICH_VTR_EL2 = 555
    ID_AA64AFR0_EL1 = 556
    ID_AA64AFR1_EL1 = 557
    ID_AA64DFR0_EL1 = 558
    ID_AA64DFR1_EL1 = 559
    ID_AA64ISAR0_EL1 = 560
    ID_AA64ISAR1_EL1 = 561
    ID_AA64MMFR0_EL1 = 562
    ID_AA64MMFR1_EL1 = 563
    ID_AA64MMFR2_EL1 = 564
    ID_AA64PFR0_EL1 = 565
    ID_AA64PFR1_EL1 = 566
    ID_AA64ZFR0_EL1 = 567
    ID_AFR0_EL1 = 568
    ID_DFR0_EL1 = 569
    ID_ISAR0_EL1 = 570
    ID_ISAR1_EL1 = 571
    ID_ISAR2_EL1 = 572
    ID_ISAR3_EL1 = 573
    ID_ISAR4_EL1 = 574
    ID_ISAR5_EL1 = 575
    ID_ISAR6_EL1 = 576
    ID_MMFR0_EL1 = 577
    ID_MMFR1_EL1 = 578
    ID_MMFR2_EL1 = 579
    ID_MMFR3_EL1 = 580
    ID_MMFR4_EL1 = 581
    ID_PFR0_EL1 = 582
    ID_PFR1_EL1 = 583
    IFSR32_EL2 = 584
    ISR_EL1 = 585
    LORC_EL1 = 586
    LOREA_EL1 = 587
    LORID_EL1 = 588
    LORN_EL1 = 589
    LORSA_EL1 = 590
    MAIR_EL1 = 591
    MAIR_EL12 = 592
    MAIR_EL2 = 593
    MAIR_EL3 = 594
    MDCCINT_EL1 = 595
    MDCCSR_EL0 = 596
    MDCR_EL2 = 597
    MDCR_EL3 = 598
    MDRAR_EL1 = 599
    MDSCR_EL1 = 600
    MIDR_EL1 = 601
    MPAM0_EL1 = 602
    MPAM1_EL1 = 603
    MPAM1_EL12 = 604
    MPAM2_EL2 = 605
    MPAM3_EL3 = 606
    MPAMHCR_EL2 = 607
    MPAMIDR_EL1 = 608
    MPAMVPM0_EL2 = 609
    MPAMVPM1_EL2 = 610
    MPAMVPM2_EL2 = 611
    MPAMVPM3_EL2 = 612
    MPAMVPM4_EL2 = 613
    MPAMVPM5_EL2 = 614
    MPAMVPM6_EL2 = 615
    MPAMVPM7_EL2 = 616
    MPAMVPMV_EL2 = 617
    MPIDR_EL1 = 618
    MVFR0_EL1 = 619
    MVFR1_EL1 = 620
    MVFR2_EL1 = 621
    NZCV = 622
    OSDLR_EL1 = 623
    OSDTRRX_EL1 = 624
    OSDTRTX_EL1 = 625
    OSECCR_EL1 = 626
    OSLAR_EL1 = 627
    OSLSR_EL1 = 628
    PAN = 629
    PAR_EL1 = 630
    PMBIDR_EL1 = 631
    PMBLIMITR_EL1 = 632
    PMBPTR_EL1 = 633
    PMBSR_EL1 = 634
    PMCCFILTR_EL0 = 635
    PMCCNTR_EL0 = 636
    PMCEID0_EL0 = 637
    PMCEID1_EL0 = 638
    PMCNTENCLR_EL0 = 639
    PMCNTENSET_EL0 = 640
    PMCR_EL0 = 641
    PMEVCNTR0_EL0 = 642
    PMEVCNTR10_EL0 = 643
    PMEVCNTR11_EL0 = 644
    PMEVCNTR12_EL0 = 645
    PMEVCNTR13_EL0 = 646
    PMEVCNTR14_EL0 = 647
    PMEVCNTR15_EL0 = 648
    PMEVCNTR16_EL0 = 649
    PMEVCNTR17_EL0 = 650
    PMEVCNTR18_EL0 = 651
    PMEVCNTR19_EL0 = 652
    PMEVCNTR1_EL0 = 653
    PMEVCNTR20_EL0 = 654
    PMEVCNTR21_EL0 = 655
    PMEVCNTR22_EL0 = 656
    PMEVCNTR23_EL0 = 657
    PMEVCNTR24_EL0 = 658
    PMEVCNTR25_EL0 = 659
    PMEVCNTR26_EL0 = 660
    PMEVCNTR27_EL0 = 661
    PMEVCNTR28_EL0 = 662
    PMEVCNTR29_EL0 = 663
    PMEVCNTR2_EL0 = 664
    PMEVCNTR30_EL0 = 665
    PMEVCNTR3_EL0 = 666
    PMEVCNTR4_EL0 = 667
    PMEVCNTR5_EL0 = 668
    PMEVCNTR6_EL0 = 669
    PMEVCNTR7_EL0 = 670
    PMEVCNTR8_EL0 = 671
    PMEVCNTR9_EL0 = 672
    PMEVTYPER0_EL0 = 673
    PMEVTYPER10_EL0 = 674
    PMEVTYPER11_EL0 = 675
    PMEVTYPER12_EL0 = 676
    PMEVTYPER13_EL0 = 677
    PMEVTYPER14_EL0 = 678
    PMEVTYPER15_EL0 = 679
    PMEVTYPER16_EL0 = 680
    PMEVTYPER17_EL0 = 681
    PMEVTYPER18_EL0 = 682
    PMEVTYPER19_EL0 = 683
    PMEVTYPER1_EL0 = 684
    PMEVTYPER20_EL0 = 685
    PMEVTYPER21_EL0 = 686
    PMEVTYPER22_EL0 = 687
    PMEVTYPER23_EL0 = 688
    PMEVTYPER24_EL0 = 689
    PMEVTYPER25_EL0 = 690
    PMEVTYPER26_EL0 = 691
    PMEVTYPER27_EL0 = 692
    PMEVTYPER28_EL0 = 693
    PMEVTYPER29_EL0 = 694
    PMEVTYPER2_EL0 = 695
    PMEVTYPER30_EL0 = 696
    PMEVTYPER3_EL0 = 697
    PMEVTYPER4_EL0 = 698
    PMEVTYPER5_EL0 = 699
    PMEVTYPER6_EL0 = 700
    PMEVTYPER7_EL0 = 701
    PMEVTYPER8_EL0 = 702
    PMEVTYPER9_EL0 = 703
    PMINTENCLR_EL1 = 704
    PMINTENSET_EL1 = 705
    PMOVSCLR_EL0 = 706
    PMOVSSET_EL0 = 707
    PMSCR_EL1 = 708
    PMSCR_EL12 = 709
    PMSCR_EL2 = 710
    PMSELR_EL0 = 711
    PMSEVFR_EL1 = 712
    PMSFCR_EL1 = 713
    PMSICR_EL1 = 714
    PMSIDR_EL1 = 715
    PMSIRR_EL1 = 716
    PMSLATFR_EL1 = 717
    PMSWINC_EL0 = 718
    PMUSERENR_EL0 = 719
    PMXEVCNTR_EL0 = 720
    PMXEVTYPER_EL0 = 721
    REVIDR_EL1 = 722
    RMR_EL1 = 723
    RMR_EL2 = 724
    RMR_EL3 = 725
    RVBAR_EL1 = 726
    RVBAR_EL2 = 727
    RVBAR_EL3 = 728
    SCR_EL3 = 729
    SCTLR_EL1 = 730
    SCTLR_EL12 = 731
    SCTLR_EL2 = 732
    SCTLR_EL3 = 733
    SDER32_EL2 = 734
    SDER32_EL3 = 735
    SPSEL = 736
    SPSR_ABT = 737
    SPSR_EL1 = 738
    SPSR_EL12 = 739
    SPSR_EL2 = 740
    SPSR_EL3 = 741
    SPSR_FIQ = 742
    SPSR_IRQ = 743
    SPSR_UND = 744
    SP_EL0 = 745
    SP_EL1 = 746
    SP_EL2 = 747
    TCR_EL1 = 748
    TCR_EL12 = 749
    TCR_EL2 = 750
    TCR_EL3 = 751
    TEECR32_EL1 = 752
    TEEHBR32_EL1 = 753
    TPIDRRO_EL0 = 754
    TPIDR_EL0 = 755
    TPIDR_EL1 = 756
    TPIDR_EL2 = 757
    TPIDR_EL3 = 758
    TRCACATR0 = 759
    TRCACATR1 = 760
    TRCACATR10 = 761
    TRCACATR11 = 762
    TRCACATR12 = 763
    TRCACATR13 = 764
    TRCACATR14 = 765
    TRCACATR15 = 766
    TRCACATR2 = 767
    TRCACATR3 = 768
    TRCACATR4 = 769
    TRCACATR5 = 770
    TRCACATR6 = 771
    TRCACATR7 = 772
    TRCACATR8 = 773
    TRCACATR9 = 774
    TRCACVR0 = 775
    TRCACVR1 = 776
    TRCACVR10 = 777
    TRCACVR11 = 778
    TRCACVR12 = 779
    TRCACVR13 = 780
    TRCACVR14 = 781
    TRCACVR15 = 782
    TRCACVR2 = 783
    TRCACVR3 = 784
    TRCACVR4 = 785
    TRCACVR5 = 786
    TRCACVR6 = 787
    TRCACVR7 = 788
    TRCACVR8 = 789
    TRCACVR9 = 790
    TRCAUTHSTATUS = 791
    TRCAUXCTLR = 792
    TRCBBCTLR = 793
    TRCCCCTLR = 794
    TRCCIDCCTLR0 = 795
    TRCCIDCCTLR1 = 796
    TRCCIDCVR0 = 797
    TRCCIDCVR1 = 798
    TRCCIDCVR2 = 799
    TRCCIDCVR3 = 800
    TRCCIDCVR4 = 801
    TRCCIDCVR5 = 802
    TRCCIDCVR6 = 803
    TRCCIDCVR7 = 804
    TRCCIDR0 = 805
    TRCCIDR1 = 806
    TRCCIDR2 = 807
    TRCCIDR3 = 808
    TRCCLAIMCLR = 809
    TRCCLAIMSET = 810
    TRCCNTCTLR0 = 811
    TRCCNTCTLR1 = 812
    TRCCNTCTLR2 = 813
    TRCCNTCTLR3 = 814
    TRCCNTRLDVR0 = 815
    TRCCNTRLDVR1 = 816
    TRCCNTRLDVR2 = 817
    TRCCNTRLDVR3 = 818
    TRCCNTVR0 = 819
    TRCCNTVR1 = 820
    TRCCNTVR2 = 821
    TRCCNTVR3 = 822
    TRCCONFIGR = 823
    TRCDEVAFF0 = 824
    TRCDEVAFF1 = 825
    TRCDEVARCH = 826
    TRCDEVID = 827
    TRCDEVTYPE = 828
    TRCDVCMR0 = 829
    TRCDVCMR1 = 830
    TRCDVCMR2 = 831
    TRCDVCMR3 = 832
    TRCDVCMR4 = 833
    TRCDVCMR5 = 834
    TRCDVCMR6 = 835
    TRCDVCMR7 = 836
    TRCDVCVR0 = 837
    TRCDVCVR1 = 838
    TRCDVCVR2 = 839
    TRCDVCVR3 = 840
    TRCDVCVR4 = 841
    TRCDVCVR5 = 842
    TRCDVCVR6 = 843
    TRCDVCVR7 = 844
    TRCEVENTCTL0R = 845
    TRCEVENTCTL1R = 846
    TRCEXTINSELR = 847
    TRCIDR0 = 848
    TRCIDR1 = 849
    TRCIDR10 = 850
    TRCIDR11 = 851
    TRCIDR12 = 852
    TRCIDR13 = 853
    TRCIDR2 = 854
    TRCIDR3 = 855
    TRCIDR4 = 856
    TRCIDR5 = 857
    TRCIDR6 = 858
    TRCIDR7 = 859
    TRCIDR8 = 860
    TRCIDR9 = 861
    TRCIMSPEC0 = 862
    TRCIMSPEC1 = 863
    TRCIMSPEC2 = 864
    TRCIMSPEC3 = 865
    TRCIMSPEC4 = 866
    TRCIMSPEC5 = 867
    TRCIMSPEC6 = 868
    TRCIMSPEC7 = 869
    TRCITCTRL = 870
    TRCLAR = 871
    TRCLSR = 872
    TRCOSLAR = 873
    TRCOSLSR = 874
    TRCPDCR = 875
    TRCPDSR = 876
    TRCPIDR0 = 877
    TRCPIDR1 = 878
    TRCPIDR2 = 879
    TRCPIDR3 = 880
    TRCPIDR4 = 881
    TRCPIDR5 = 882
    TRCPIDR6 = 883
    TRCPIDR7 = 884
    TRCPRGCTLR = 885
    TRCPROCSELR = 886
    TRCQCTLR = 887
    TRCRSCTLR10 = 888
    TRCRSCTLR11 = 889
    TRCRSCTLR12 = 890
    TRCRSCTLR13 = 891
    TRCRSCTLR14 = 892
    TRCRSCTLR15 = 893
    TRCRSCTLR16 = 894
    TRCRSCTLR17 = 895
    TRCRSCTLR18 = 896
    TRCRSCTLR19 = 897
    TRCRSCTLR2 = 898
    TRCRSCTLR20 = 899
    TRCRSCTLR21 = 900
    TRCRSCTLR22 = 901
    TRCRSCTLR23 = 902
    TRCRSCTLR24 = 903
    TRCRSCTLR25 = 904
    TRCRSCTLR26 = 905
    TRCRSCTLR27 = 906
    TRCRSCTLR28 = 907
    TRCRSCTLR29 = 908
    TRCRSCTLR3 = 909
    TRCRSCTLR30 = 910
    TRCRSCTLR31 = 911
    TRCRSCTLR4 = 912
    TRCRSCTLR5 = 913
    TRCRSCTLR6 = 914
    TRCRSCTLR7 = 915
    TRCRSCTLR8 = 916
    TRCRSCTLR9 = 917
    TRCSEQEVR0 = 918
    TRCSEQEVR1 = 919
    TRCSEQEVR2 = 920
    TRCSEQRSTEVR = 921
    TRCSEQSTR = 922
    TRCSSCCR0 = 923
    TRCSSCCR1 = 924
    TRCSSCCR2 = 925
    TRCSSCCR3 = 926
    TRCSSCCR4 = 927
    TRCSSCCR5 = 928
    TRCSSCCR6 = 929
    TRCSSCCR7 = 930
    TRCSSCSR0 = 931
    TRCSSCSR1 = 932
    TRCSSCSR2 = 933
    TRCSSCSR3 = 934
    TRCSSCSR4 = 935
    TRCSSCSR5 = 936
    TRCSSCSR6 = 937
    TRCSSCSR7 = 938
    TRCSSPCICR0 = 939
    TRCSSPCICR1 = 940
    TRCSSPCICR2 = 941
    TRCSSPCICR3 = 942
    TRCSSPCICR4 = 943
    TRCSSPCICR5 = 944
    TRCSSPCICR6 = 945
    TRCSSPCICR7 = 946
    TRCSTALLCTLR = 947
    TRCSTATR = 948
    TRCSYNCPR = 949
    TRCTRACEIDR = 950
    TRCTSCTLR = 951
    TRCVDARCCTLR = 952
    TRCVDCTLR = 953
    TRCVDSACCTLR = 954
    TRCVICTLR = 955
    TRCVIIECTLR = 956
    TRCVIPCSSCTLR = 957
    TRCVISSCTLR = 958
    TRCVMIDCCTLR0 = 959
    TRCVMIDCCTLR1 = 960
    TRCVMIDCVR0 = 961
    TRCVMIDCVR1 = 962
    TRCVMIDCVR2 = 963
    TRCVMIDCVR3 = 964
    TRCVMIDCVR4 = 965
    TRCVMIDCVR5 = 966
    TRCVMIDCVR6 = 967
    TRCVMIDCVR7 = 968
    TRFCR_EL1 = 969
    TRFCR_EL12 = 970
    TRFCR_EL2 = 971
    TTBR0_EL1 = 972
    TTBR0_EL12 = 973
    TTBR0_EL2 = 974
    TTBR0_EL3 = 975
    TTBR1_EL1 = 976
    TTBR1_EL12 = 977
    TTBR1_EL2 = 978
    UAO = 979
    VBAR_EL1 = 980
    VBAR_EL12 = 981
    VBAR_EL2 = 982
    VBAR_EL3 = 983
    VDISR_EL2 = 984
    VMPIDR_EL2 = 985
    VNCR_EL2 = 986
    VPIDR_EL2 = 987
    VSESR_EL2 = 988
    VSTCR_EL2 = 989
    VSTTBR_EL2 = 990
    VTCR_EL2 = 991
    VTTBR_EL2 = 992
    ZCR_EL1 = 993
    ZCR_EL12 = 994
    ZCR_EL2 = 995
    ZCR_EL3 = 996


class X86_class:

    EAX = 41
    AX = 42
    AH = 43
    AL = 44
    EBX = 45
    BX = 46
    BH = 47
    BL = 48
    ECX = 49
    CX = 50
    CH = 51
    CL = 52
    EDX = 53
    DX = 54
    DH = 55
    DL = 56
    EDI = 57
    DI = 58
    DIL = 59
    ESI = 60
    SI = 61
    SIL = 62
    EBP = 63
    BP = 64
    BPL = 65
    ESP = 66
    SP = 67
    SPL = 68
    EIP = 69
    IP = 70
    EFLAGS = 71
    MM0 = 72
    MM1 = 73
    MM2 = 74
    MM3 = 75
    MM4 = 76
    MM5 = 77
    MM6 = 78
    MM7 = 79
    ST0 = 80
    ST1 = 81
    ST2 = 82
    ST3 = 83
    ST4 = 84
    ST5 = 85
    ST6 = 86
    ST7 = 87
    FTW = 88
    FCW = 89
    FSW = 90
    FOP = 91
    FCS = 92
    FDS = 93
    FIP = 94
    FDP = 95
    MXCSR = 96
    MXCSR_MASK = 97
    XMM0 = 98
    XMM1 = 99
    XMM2 = 100
    XMM3 = 101
    XMM4 = 102
    XMM5 = 103
    XMM6 = 104
    XMM7 = 105
    YMM0 = 130
    YMM1 = 131
    YMM2 = 132
    YMM3 = 133
    YMM4 = 134
    YMM5 = 135
    YMM6 = 136
    YMM7 = 137
    CR0 = 194
    CR1 = 195
    CR2 = 196
    CR3 = 197
    CR4 = 198
    CR5 = 199
    CR6 = 200
    CR7 = 201
    CR8 = 202
    CR9 = 203
    CR10 = 204
    CR11 = 205
    CR12 = 206
    CR13 = 207
    CR14 = 208
    CR15 = 209
    DR0 = 210
    DR1 = 211
    DR2 = 212
    DR3 = 213
    DR6 = 214
    DR7 = 215
    AC = 216
    AF = 217
    CF = 218
    DF = 219
    ID = 220
    IF = 221
    NT = 222
    OF = 223
    PF = 224
    RF = 225
    SF = 226
    TF = 227
    VIF = 228
    VIP = 229
    VM = 230
    ZF = 231
    SSE_IE = 232
    SSE_DE = 233
    SSE_ZE = 234
    SSE_OE = 235
    SSE_UE = 236
    SSE_PE = 237
    SSE_DAZ = 238
    SSE_IM = 239
    SSE_DM = 240
    SSE_ZM = 241
    SSE_OM = 242
    SSE_UM = 243
    SSE_PM = 244
    SSE_RL = 245
    SSE_RH = 246
    SSE_FZ = 247
    FCW_IM = 248
    FCW_DM = 249
    FCW_ZM = 250
    FCW_OM = 251
    FCW_UM = 252
    FCW_PM = 253
    FCW_PC = 254
    FCW_RC = 255
    FCW_X = 256
    FSW_IE = 257
    FSW_DE = 258
    FSW_ZE = 259
    FSW_OE = 260
    FSW_UE = 261
    FSW_PE = 262
    FSW_SF = 263
    FSW_ES = 264
    FSW_C0 = 265
    FSW_C1 = 266
    FSW_C2 = 267
    FSW_TOP = 268
    FSW_C3 = 269
    FSW_B = 270
    CS = 280
    DS = 281
    ES = 282
    FS = 283
    GS = 284
    SS = 285
    TSC = 286


class X86_64_class:

    RAX = 0
    RBX = 1
    RCX = 2
    RDX = 3
    RDI = 4
    RSI = 5
    RBP = 6
    RSP = 7
    RIP = 8
    R8 = 9
    R8D = 10
    R8W = 11
    R8B = 12
    R9 = 13
    R9D = 14
    R9W = 15
    R9B = 16
    R10 = 17
    R10D = 18
    R10W = 19
    R10B = 20
    R11 = 21
    R11D = 22
    R11W = 23
    R11B = 24
    R12 = 25
    R12D = 26
    R12W = 27
    R12B = 28
    R13 = 29
    R13D = 30
    R13W = 31
    R13B = 32
    R14 = 33
    R14D = 34
    R14W = 35
    R14B = 36
    R15 = 37
    R15D = 38
    R15W = 39
    R15B = 40
    EAX = 41
    AX = 42
    AH = 43
    AL = 44
    EBX = 45
    BX = 46
    BH = 47
    BL = 48
    ECX = 49
    CX = 50
    CH = 51
    CL = 52
    EDX = 53
    DX = 54
    DH = 55
    DL = 56
    EDI = 57
    DI = 58
    DIL = 59
    ESI = 60
    SI = 61
    SIL = 62
    EBP = 63
    BP = 64
    BPL = 65
    ESP = 66
    SP = 67
    SPL = 68
    EIP = 69
    IP = 70
    EFLAGS = 71
    MM0 = 72
    MM1 = 73
    MM2 = 74
    MM3 = 75
    MM4 = 76
    MM5 = 77
    MM6 = 78
    MM7 = 79
    ST0 = 80
    ST1 = 81
    ST2 = 82
    ST3 = 83
    ST4 = 84
    ST5 = 85
    ST6 = 86
    ST7 = 87
    FTW = 88
    FCW = 89
    FSW = 90
    FOP = 91
    FCS = 92
    FDS = 93
    FIP = 94
    FDP = 95
    MXCSR = 96
    MXCSR_MASK = 97
    XMM0 = 98
    XMM1 = 99
    XMM2 = 100
    XMM3 = 101
    XMM4 = 102
    XMM5 = 103
    XMM6 = 104
    XMM7 = 105
    XMM8 = 106
    XMM9 = 107
    XMM10 = 108
    XMM11 = 109
    XMM12 = 110
    XMM13 = 111
    XMM14 = 112
    XMM15 = 113
    XMM16 = 114
    XMM17 = 115
    XMM18 = 116
    XMM19 = 117
    XMM20 = 118
    XMM21 = 119
    XMM22 = 120
    XMM23 = 121
    XMM24 = 122
    XMM25 = 123
    XMM26 = 124
    XMM27 = 125
    XMM28 = 126
    XMM29 = 127
    XMM30 = 128
    XMM31 = 129
    YMM0 = 130
    YMM1 = 131
    YMM2 = 132
    YMM3 = 133
    YMM4 = 134
    YMM5 = 135
    YMM6 = 136
    YMM7 = 137
    YMM8 = 138
    YMM9 = 139
    YMM10 = 140
    YMM11 = 141
    YMM12 = 142
    YMM13 = 143
    YMM14 = 144
    YMM15 = 145
    YMM16 = 146
    YMM17 = 147
    YMM18 = 148
    YMM19 = 149
    YMM20 = 150
    YMM21 = 151
    YMM22 = 152
    YMM23 = 153
    YMM24 = 154
    YMM25 = 155
    YMM26 = 156
    YMM27 = 157
    YMM28 = 158
    YMM29 = 159
    YMM30 = 160
    YMM31 = 161
    ZMM0 = 162
    ZMM1 = 163
    ZMM2 = 164
    ZMM3 = 165
    ZMM4 = 166
    ZMM5 = 167
    ZMM6 = 168
    ZMM7 = 169
    ZMM8 = 170
    ZMM9 = 171
    ZMM10 = 172
    ZMM11 = 173
    ZMM12 = 174
    ZMM13 = 175
    ZMM14 = 176
    ZMM15 = 177
    ZMM16 = 178
    ZMM17 = 179
    ZMM18 = 180
    ZMM19 = 181
    ZMM20 = 182
    ZMM21 = 183
    ZMM22 = 184
    ZMM23 = 185
    ZMM24 = 186
    ZMM25 = 187
    ZMM26 = 188
    ZMM27 = 189
    ZMM28 = 190
    ZMM29 = 191
    ZMM30 = 192
    ZMM31 = 193
    CR0 = 194
    CR1 = 195
    CR2 = 196
    CR3 = 197
    CR4 = 198
    CR5 = 199
    CR6 = 200
    CR7 = 201
    CR8 = 202
    CR9 = 203
    CR10 = 204
    CR11 = 205
    CR12 = 206
    CR13 = 207
    CR14 = 208
    CR15 = 209
    DR0 = 210
    DR1 = 211
    DR2 = 212
    DR3 = 213
    DR6 = 214
    DR7 = 215
    AC = 216
    AF = 217
    CF = 218
    DF = 219
    ID = 220
    IF = 221
    NT = 222
    OF = 223
    PF = 224
    RF = 225
    SF = 226
    TF = 227
    VIF = 228
    VIP = 229
    VM = 230
    ZF = 231
    SSE_IE = 232
    SSE_DE = 233
    SSE_ZE = 234
    SSE_OE = 235
    SSE_UE = 236
    SSE_PE = 237
    SSE_DAZ = 238
    SSE_IM = 239
    SSE_DM = 240
    SSE_ZM = 241
    SSE_OM = 242
    SSE_UM = 243
    SSE_PM = 244
    SSE_RL = 245
    SSE_RH = 246
    SSE_FZ = 247
    FCW_IM = 248
    FCW_DM = 249
    FCW_ZM = 250
    FCW_OM = 251
    FCW_UM = 252
    FCW_PM = 253
    FCW_PC = 254
    FCW_RC = 255
    FCW_X = 256
    FSW_IE = 257
    FSW_DE = 258
    FSW_ZE = 259
    FSW_OE = 260
    FSW_UE = 261
    FSW_PE = 262
    FSW_SF = 263
    FSW_ES = 264
    FSW_C0 = 265
    FSW_C1 = 266
    FSW_C2 = 267
    FSW_TOP = 268
    FSW_C3 = 269
    FSW_B = 270
    EFER = 271
    EFER_TCE = 272
    EFER_FFXSR = 273
    EFER_LMSLE = 274
    EFER_SVME = 275
    EFER_NXE = 276
    EFER_LMA = 277
    EFER_LME = 278
    EFER_SCE = 279
    CS = 280
    DS = 281
    ES = 282
    FS = 283
    GS = 284
    SS = 285
    TSC = 286


class REG:

    AARCH64 = AARCH64_class
    X86 = X86_class
    X86_64 = X86_64_class



class CPUSIZE(IntEnum):
    BYTE = 1
    BYTE_BIT = 2
    WORD = 3
    WORD_BIT = 4
    DWORD = 5
    DWORD_BIT = 6
    QWORD = 7
    QWORD_BIT = 8
    FWORD = 9
    FWORD_BIT = 10
    DQWORD = 11
    DQWORD_BIT = 12
    QQWORD = 13
    QQWORD_BIT = 14
    DQQWORD = 15
    DQQWORD_BIT = 16

class MODE(IntEnum):
    ALIGNED_MEMORY = 1
    AST_OPTIMIZATIONS = 2
    CONCRETIZE_UNDEFINED_REGISTERS = 3
    CONSTANT_FOLDING = 4
    MEMORY_ARRAY = 5
    ONLY_ON_SYMBOLIZED = 6
    ONLY_ON_TAINTED = 7
    PC_TRACKING_SYMBOLIC = 8
    SYMBOLIZE_INDEX_ROTATION = 9
    SYMBOLIZE_LOAD = 10
    SYMBOLIZE_STORE = 11
    TAINT_THROUGH_POINTERS = 12

class AST_NODE(IntEnum):
    ANY = 1
    ARRAY = 2
    ASSERT = 3
    BSWAP = 4
    BV = 5
    BVADD = 6
    BVAND = 7
    BVASHR = 8
    BVLSHR = 9
    BVMUL = 10
    BVNAND = 11
    BVNEG = 12
    BVNOR = 13
    BVNOT = 14
    BVOR = 15
    BVROL = 16
    BVROR = 17
    BVSDIV = 18
    BVSGE = 19
    BVSGT = 20
    BVSHL = 21
    BVSLE = 22
    BVSLT = 23
    BVSMOD = 24
    BVSREM = 25
    BVSUB = 26
    BVUDIV = 27
    BVUGE = 28
    BVUGT = 29
    BVULE = 30
    BVULT = 31
    BVUREM = 32
    BVXNOR = 33
    BVXOR = 34
    COMPOUND = 35
    CONCAT = 36
    DECLARE = 37
    DISTINCT = 38
    EQUAL = 39
    EXTRACT = 40
    FORALL = 41
    IFF = 42
    INTEGER = 43
    INVALID = 44
    ITE = 45
    LAND = 46
    LET = 47
    LNOT = 48
    LOR = 49
    REFERENCE = 50
    SELECT = 51
    STORE = 52
    STRING = 53
    SX = 54
    VARIABLE = 55
    ZX = 56

class AST_REPRESENTATION(IntEnum):
    SMT = 1
    PCODE = 2
    PYTHON = 3

class OPCODE(IntEnum):
    pass
    class X86(IntEnum):
        INVALID = 1
        AAA = 2
        AAD = 3
        AAM = 4
        AAS = 5
        FABS = 6
        ADC = 7
        ADCX = 8
        ADD = 9
        ADDPD = 10
        ADDPS = 11
        ADDSD = 12
        ADDSS = 13
        ADDSUBPD = 14
        ADDSUBPS = 15
        FADD = 16
        FIADD = 17
        FADDP = 18
        ADOX = 19
        AESDECLAST = 20
        AESDEC = 21
        AESENCLAST = 22
        AESENC = 23
        AESIMC = 24
        AESKEYGENASSIST = 25
        AND = 26
        ANDN = 27
        ANDNPD = 28
        ANDNPS = 29
        ANDPD = 30
        ANDPS = 31
        ARPL = 32
        BEXTR = 33
        BLCFILL = 34
        BLCI = 35
        BLCIC = 36
        BLCMSK = 37
        BLCS = 38
        BLENDPD = 39
        BLENDPS = 40
        BLENDVPD = 41
        BLENDVPS = 42
        BLSFILL = 43
        BLSI = 44
        BLSIC = 45
        BLSMSK = 46
        BLSR = 47
        BOUND = 48
        BSF = 49
        BSR = 50
        BSWAP = 51
        BT = 52
        BTC = 53
        BTR = 54
        BTS = 55
        BZHI = 56
        CALL = 57
        CBW = 58
        CDQ = 59
        CDQE = 60
        FCHS = 61
        CLAC = 62
        CLC = 63
        CLD = 64
        CLFLUSH = 65
        CLGI = 66
        CLI = 67
        CLTS = 68
        CMC = 69
        CMOVA = 70
        CMOVAE = 71
        CMOVB = 72
        CMOVBE = 73
        FCMOVBE = 74
        FCMOVB = 75
        CMOVE = 76
        FCMOVE = 77
        CMOVG = 78
        CMOVGE = 79
        CMOVL = 80
        CMOVLE = 81
        FCMOVNBE = 82
        FCMOVNB = 83
        CMOVNE = 84
        FCMOVNE = 85
        CMOVNO = 86
        CMOVNP = 87
        FCMOVNU = 88
        CMOVNS = 89
        CMOVO = 90
        CMOVP = 91
        FCMOVU = 92
        CMOVS = 93
        CMP = 94
        CMPPD = 95
        CMPPS = 96
        CMPSB = 97
        CMPSD = 98
        CMPSQ = 99
        CMPSS = 100
        CMPSW = 101
        CMPXCHG16B = 102
        CMPXCHG = 103
        CMPXCHG8B = 104
        COMISD = 105
        COMISS = 106
        FCOMP = 107
        FCOMPI = 108
        FCOMI = 109
        FCOM = 110
        FCOS = 111
        CPUID = 112
        CQO = 113
        CRC32 = 114
        CVTDQ2PD = 115
        CVTDQ2PS = 116
        CVTPD2DQ = 117
        CVTPD2PS = 118
        CVTPS2DQ = 119
        CVTPS2PD = 120
        CVTSD2SI = 121
        CVTSD2SS = 122
        CVTSI2SD = 123
        CVTSI2SS = 124
        CVTSS2SD = 125
        CVTSS2SI = 126
        CVTTPD2DQ = 127
        CVTTPS2DQ = 128
        CVTTSD2SI = 129
        CVTTSS2SI = 130
        CWD = 131
        CWDE = 132
        DAA = 133
        DAS = 134
        DATA16 = 135
        DEC = 136
        DIV = 137
        DIVPD = 138
        DIVPS = 139
        FDIVR = 140
        FIDIVR = 141
        FDIVRP = 142
        DIVSD = 143
        DIVSS = 144
        FDIV = 145
        FIDIV = 146
        FDIVP = 147
        DPPD = 148
        DPPS = 149
        RET = 150
        ENCLS = 151
        ENCLU = 152
        ENTER = 153
        EXTRACTPS = 154
        EXTRQ = 155
        F2XM1 = 156
        LCALL = 157
        LJMP = 158
        FBLD = 159
        FBSTP = 160
        FCOMPP = 161
        FDECSTP = 162
        FEMMS = 163
        FFREE = 164
        FICOM = 165
        FICOMP = 166
        FINCSTP = 167
        FLDCW = 168
        FLDENV = 169
        FLDL2E = 170
        FLDL2T = 171
        FLDLG2 = 172
        FLDLN2 = 173
        FLDPI = 174
        FNCLEX = 175
        FNINIT = 176
        FNOP = 177
        FNSTCW = 178
        FNSTSW = 179
        FPATAN = 180
        FPREM = 181
        FPREM1 = 182
        FPTAN = 183
        FRNDINT = 184
        FRSTOR = 185
        FNSAVE = 186
        FSCALE = 187
        FSETPM = 188
        FSINCOS = 189
        FNSTENV = 190
        FXAM = 191
        FXRSTOR = 192
        FXRSTOR64 = 193
        FXSAVE = 194
        FXSAVE64 = 195
        FXTRACT = 196
        FYL2X = 197
        FYL2XP1 = 198
        MOVAPD = 199
        MOVAPS = 200
        ORPD = 201
        ORPS = 202
        VMOVAPD = 203
        VMOVAPS = 204
        XORPD = 205
        XORPS = 206
        GETSEC = 207
        HADDPD = 208
        HADDPS = 209
        HLT = 210
        HSUBPD = 211
        HSUBPS = 212
        IDIV = 213
        FILD = 214
        IMUL = 215
        IN = 216
        INC = 217
        INSB = 218
        INSERTPS = 219
        INSERTQ = 220
        INSD = 221
        INSW = 222
        INT = 223
        INT1 = 224
        INT3 = 225
        INTO = 226
        INVD = 227
        INVEPT = 228
        INVLPG = 229
        INVLPGA = 230
        INVPCID = 231
        INVVPID = 232
        IRET = 233
        IRETD = 234
        IRETQ = 235
        FISTTP = 236
        FIST = 237
        FISTP = 238
        UCOMISD = 239
        UCOMISS = 240
        VCMP = 241
        VCOMISD = 242
        VCOMISS = 243
        VCVTSD2SS = 244
        VCVTSI2SD = 245
        VCVTSI2SS = 246
        VCVTSS2SD = 247
        VCVTTSD2SI = 248
        VCVTTSD2USI = 249
        VCVTTSS2SI = 250
        VCVTTSS2USI = 251
        VCVTUSI2SD = 252
        VCVTUSI2SS = 253
        VUCOMISD = 254
        VUCOMISS = 255
        JAE = 256
        JA = 257
        JBE = 258
        JB = 259
        JCXZ = 260
        JECXZ = 261
        JE = 262
        JGE = 263
        JG = 264
        JLE = 265
        JL = 266
        JMP = 267
        JNE = 268
        JNO = 269
        JNP = 270
        JNS = 271
        JO = 272
        JP = 273
        JRCXZ = 274
        JS = 275
        KANDB = 276
        KANDD = 277
        KANDNB = 278
        KANDND = 279
        KANDNQ = 280
        KANDNW = 281
        KANDQ = 282
        KANDW = 283
        KMOVB = 284
        KMOVD = 285
        KMOVQ = 286
        KMOVW = 287
        KNOTB = 288
        KNOTD = 289
        KNOTQ = 290
        KNOTW = 291
        KORB = 292
        KORD = 293
        KORQ = 294
        KORTESTW = 295
        KORW = 296
        KSHIFTLW = 297
        KSHIFTRW = 298
        KUNPCKBW = 299
        KXNORB = 300
        KXNORD = 301
        KXNORQ = 302
        KXNORW = 303
        KXORB = 304
        KXORD = 305
        KXORQ = 306
        KXORW = 307
        LAHF = 308
        LAR = 309
        LDDQU = 310
        LDMXCSR = 311
        LDS = 312
        FLDZ = 313
        FLD1 = 314
        FLD = 315
        LEA = 316
        LEAVE = 317
        LES = 318
        LFENCE = 319
        LFS = 320
        LGDT = 321
        LGS = 322
        LIDT = 323
        LLDT = 324
        LMSW = 325
        OR = 326
        SUB = 327
        XOR = 328
        LODSB = 329
        LODSD = 330
        LODSQ = 331
        LODSW = 332
        LOOP = 333
        LOOPE = 334
        LOOPNE = 335
        RETF = 336
        RETFQ = 337
        LSL = 338
        LSS = 339
        LTR = 340
        XADD = 341
        LZCNT = 342
        MASKMOVDQU = 343
        MAXPD = 344
        MAXPS = 345
        MAXSD = 346
        MAXSS = 347
        MFENCE = 348
        MINPD = 349
        MINPS = 350
        MINSD = 351
        MINSS = 352
        CVTPD2PI = 353
        CVTPI2PD = 354
        CVTPI2PS = 355
        CVTPS2PI = 356
        CVTTPD2PI = 357
        CVTTPS2PI = 358
        EMMS = 359
        MASKMOVQ = 360
        MOVD = 361
        MOVDQ2Q = 362
        MOVNTQ = 363
        MOVQ2DQ = 364
        MOVQ = 365
        PABSB = 366
        PABSD = 367
        PABSW = 368
        PACKSSDW = 369
        PACKSSWB = 370
        PACKUSWB = 371
        PADDB = 372
        PADDD = 373
        PADDQ = 374
        PADDSB = 375
        PADDSW = 376
        PADDUSB = 377
        PADDUSW = 378
        PADDW = 379
        PALIGNR = 380
        PANDN = 381
        PAND = 382
        PAVGB = 383
        PAVGW = 384
        PCMPEQB = 385
        PCMPEQD = 386
        PCMPEQW = 387
        PCMPGTB = 388
        PCMPGTD = 389
        PCMPGTW = 390
        PEXTRW = 391
        PHADDSW = 392
        PHADDW = 393
        PHADDD = 394
        PHSUBD = 395
        PHSUBSW = 396
        PHSUBW = 397
        PINSRW = 398
        PMADDUBSW = 399
        PMADDWD = 400
        PMAXSW = 401
        PMAXUB = 402
        PMINSW = 403
        PMINUB = 404
        PMOVMSKB = 405
        PMULHRSW = 406
        PMULHUW = 407
        PMULHW = 408
        PMULLW = 409
        PMULUDQ = 410
        POR = 411
        PSADBW = 412
        PSHUFB = 413
        PSHUFW = 414
        PSIGNB = 415
        PSIGND = 416
        PSIGNW = 417
        PSLLD = 418
        PSLLQ = 419
        PSLLW = 420
        PSRAD = 421
        PSRAW = 422
        PSRLD = 423
        PSRLQ = 424
        PSRLW = 425
        PSUBB = 426
        PSUBD = 427
        PSUBQ = 428
        PSUBSB = 429
        PSUBSW = 430
        PSUBUSB = 431
        PSUBUSW = 432
        PSUBW = 433
        PUNPCKHBW = 434
        PUNPCKHDQ = 435
        PUNPCKHWD = 436
        PUNPCKLBW = 437
        PUNPCKLDQ = 438
        PUNPCKLWD = 439
        PXOR = 440
        MONITOR = 441
        MONTMUL = 442
        MOV = 443
        MOVABS = 444
        MOVBE = 445
        MOVDDUP = 446
        MOVDQA = 447
        MOVDQU = 448
        MOVHLPS = 449
        MOVHPD = 450
        MOVHPS = 451
        MOVLHPS = 452
        MOVLPD = 453
        MOVLPS = 454
        MOVMSKPD = 455
        MOVMSKPS = 456
        MOVNTDQA = 457
        MOVNTDQ = 458
        MOVNTI = 459
        MOVNTPD = 460
        MOVNTPS = 461
        MOVNTSD = 462
        MOVNTSS = 463
        MOVSB = 464
        MOVSD = 465
        MOVSHDUP = 466
        MOVSLDUP = 467
        MOVSQ = 468
        MOVSS = 469
        MOVSW = 470
        MOVSX = 471
        MOVSXD = 472
        MOVUPD = 473
        MOVUPS = 474
        MOVZX = 475
        MPSADBW = 476
        MUL = 477
        MULPD = 478
        MULPS = 479
        MULSD = 480
        MULSS = 481
        MULX = 482
        FMUL = 483
        FIMUL = 484
        FMULP = 485
        MWAIT = 486
        NEG = 487
        NOP = 488
        NOT = 489
        OUT = 490
        OUTSB = 491
        OUTSD = 492
        OUTSW = 493
        PACKUSDW = 494
        PAUSE = 495
        PAVGUSB = 496
        PBLENDVB = 497
        PBLENDW = 498
        PCLMULQDQ = 499
        PCMPEQQ = 500
        PCMPESTRI = 501
        PCMPESTRM = 502
        PCMPGTQ = 503
        PCMPISTRI = 504
        PCMPISTRM = 505
        PDEP = 506
        PEXT = 507
        PEXTRB = 508
        PEXTRD = 509
        PEXTRQ = 510
        PF2ID = 511
        PF2IW = 512
        PFACC = 513
        PFADD = 514
        PFCMPEQ = 515
        PFCMPGE = 516
        PFCMPGT = 517
        PFMAX = 518
        PFMIN = 519
        PFMUL = 520
        PFNACC = 521
        PFPNACC = 522
        PFRCPIT1 = 523
        PFRCPIT2 = 524
        PFRCP = 525
        PFRSQIT1 = 526
        PFRSQRT = 527
        PFSUBR = 528
        PFSUB = 529
        PHMINPOSUW = 530
        PI2FD = 531
        PI2FW = 532
        PINSRB = 533
        PINSRD = 534
        PINSRQ = 535
        PMAXSB = 536
        PMAXSD = 537
        PMAXUD = 538
        PMAXUW = 539
        PMINSB = 540
        PMINSD = 541
        PMINUD = 542
        PMINUW = 543
        PMOVSXBD = 544
        PMOVSXBQ = 545
        PMOVSXBW = 546
        PMOVSXDQ = 547
        PMOVSXWD = 548
        PMOVSXWQ = 549
        PMOVZXBD = 550
        PMOVZXBQ = 551
        PMOVZXBW = 552
        PMOVZXDQ = 553
        PMOVZXWD = 554
        PMOVZXWQ = 555
        PMULDQ = 556
        PMULHRW = 557
        PMULLD = 558
        POP = 559
        POPAW = 560
        POPAL = 561
        POPCNT = 562
        POPF = 563
        POPFD = 564
        POPFQ = 565
        PREFETCH = 566
        PREFETCHNTA = 567
        PREFETCHT0 = 568
        PREFETCHT1 = 569
        PREFETCHT2 = 570
        PREFETCHW = 571
        PSHUFD = 572
        PSHUFHW = 573
        PSHUFLW = 574
        PSLLDQ = 575
        PSRLDQ = 576
        PSWAPD = 577
        PTEST = 578
        PUNPCKHQDQ = 579
        PUNPCKLQDQ = 580
        PUSH = 581
        PUSHAW = 582
        PUSHAL = 583
        PUSHF = 584
        PUSHFD = 585
        PUSHFQ = 586
        RCL = 587
        RCPPS = 588
        RCPSS = 589
        RCR = 590
        RDFSBASE = 591
        RDGSBASE = 592
        RDMSR = 593
        RDPMC = 594
        RDRAND = 595
        RDSEED = 596
        RDTSC = 597
        RDTSCP = 598
        ROL = 599
        ROR = 600
        RORX = 601
        ROUNDPD = 602
        ROUNDPS = 603
        ROUNDSD = 604
        ROUNDSS = 605
        RSM = 606
        RSQRTPS = 607
        RSQRTSS = 608
        SAHF = 609
        SAL = 610
        SALC = 611
        SAR = 612
        SARX = 613
        SBB = 614
        SCASB = 615
        SCASD = 616
        SCASQ = 617
        SCASW = 618
        SETAE = 619
        SETA = 620
        SETBE = 621
        SETB = 622
        SETE = 623
        SETGE = 624
        SETG = 625
        SETLE = 626
        SETL = 627
        SETNE = 628
        SETNO = 629
        SETNP = 630
        SETNS = 631
        SETO = 632
        SETP = 633
        SETS = 634
        SFENCE = 635
        SGDT = 636
        SHA1MSG1 = 637
        SHA1MSG2 = 638
        SHA1NEXTE = 639
        SHA1RNDS4 = 640
        SHA256MSG1 = 641
        SHA256MSG2 = 642
        SHA256RNDS2 = 643
        SHL = 644
        SHLD = 645
        SHLX = 646
        SHR = 647
        SHRD = 648
        SHRX = 649
        SHUFPD = 650
        SHUFPS = 651
        SIDT = 652
        FSIN = 653
        SKINIT = 654
        SLDT = 655
        SMSW = 656
        SQRTPD = 657
        SQRTPS = 658
        SQRTSD = 659
        SQRTSS = 660
        FSQRT = 661
        STAC = 662
        STC = 663
        STD = 664
        STGI = 665
        STI = 666
        STMXCSR = 667
        STOSB = 668
        STOSD = 669
        STOSQ = 670
        STOSW = 671
        STR = 672
        FST = 673
        FSTP = 674
        FSTPNCE = 675
        SUBPD = 676
        SUBPS = 677
        FSUBR = 678
        FISUBR = 679
        FSUBRP = 680
        SUBSD = 681
        SUBSS = 682
        FSUB = 683
        FISUB = 684
        FSUBP = 685
        SWAPGS = 686
        SYSCALL = 687
        SYSENTER = 688
        SYSEXIT = 689
        SYSRET = 690
        T1MSKC = 691
        TEST = 692
        UD2 = 693
        FTST = 694
        TZCNT = 695
        TZMSK = 696
        FUCOMPI = 697
        FUCOMI = 698
        FUCOMPP = 699
        FUCOMP = 700
        FUCOM = 701
        UD2B = 702
        UNPCKHPD = 703
        UNPCKHPS = 704
        UNPCKLPD = 705
        UNPCKLPS = 706
        VADDPD = 707
        VADDPS = 708
        VADDSD = 709
        VADDSS = 710
        VADDSUBPD = 711
        VADDSUBPS = 712
        VAESDECLAST = 713
        VAESDEC = 714
        VAESENCLAST = 715
        VAESENC = 716
        VAESIMC = 717
        VAESKEYGENASSIST = 718
        VALIGND = 719
        VALIGNQ = 720
        VANDNPD = 721
        VANDNPS = 722
        VANDPD = 723
        VANDPS = 724
        VBLENDMPD = 725
        VBLENDMPS = 726
        VBLENDPD = 727
        VBLENDPS = 728
        VBLENDVPD = 729
        VBLENDVPS = 730
        VBROADCASTF128 = 731
        VBROADCASTI128 = 732
        VBROADCASTI32X4 = 733
        VBROADCASTI64X4 = 734
        VBROADCASTSD = 735
        VBROADCASTSS = 736
        VCMPPD = 737
        VCMPPS = 738
        VCMPSD = 739
        VCMPSS = 740
        VCVTDQ2PD = 741
        VCVTDQ2PS = 742
        VCVTPD2DQX = 743
        VCVTPD2DQ = 744
        VCVTPD2PSX = 745
        VCVTPD2PS = 746
        VCVTPD2UDQ = 747
        VCVTPH2PS = 748
        VCVTPS2DQ = 749
        VCVTPS2PD = 750
        VCVTPS2PH = 751
        VCVTPS2UDQ = 752
        VCVTSD2SI = 753
        VCVTSD2USI = 754
        VCVTSS2SI = 755
        VCVTSS2USI = 756
        VCVTTPD2DQX = 757
        VCVTTPD2DQ = 758
        VCVTTPD2UDQ = 759
        VCVTTPS2DQ = 760
        VCVTTPS2UDQ = 761
        VCVTUDQ2PD = 762
        VCVTUDQ2PS = 763
        VDIVPD = 764
        VDIVPS = 765
        VDIVSD = 766
        VDIVSS = 767
        VDPPD = 768
        VDPPS = 769
        VERR = 770
        VERW = 771
        VEXTRACTF128 = 772
        VEXTRACTF32X4 = 773
        VEXTRACTF64X4 = 774
        VEXTRACTI128 = 775
        VEXTRACTI32X4 = 776
        VEXTRACTI64X4 = 777
        VEXTRACTPS = 778
        VFMADD132PD = 779
        VFMADD132PS = 780
        VFMADD213PD = 781
        VFMADD213PS = 782
        VFMADDPD = 783
        VFMADD231PD = 784
        VFMADDPS = 785
        VFMADD231PS = 786
        VFMADDSD = 787
        VFMADD213SD = 788
        VFMADD132SD = 789
        VFMADD231SD = 790
        VFMADDSS = 791
        VFMADD213SS = 792
        VFMADD132SS = 793
        VFMADD231SS = 794
        VFMADDSUB132PD = 795
        VFMADDSUB132PS = 796
        VFMADDSUB213PD = 797
        VFMADDSUB213PS = 798
        VFMADDSUBPD = 799
        VFMADDSUB231PD = 800
        VFMADDSUBPS = 801
        VFMADDSUB231PS = 802
        VFMSUB132PD = 803
        VFMSUB132PS = 804
        VFMSUB213PD = 805
        VFMSUB213PS = 806
        VFMSUBADD132PD = 807
        VFMSUBADD132PS = 808
        VFMSUBADD213PD = 809
        VFMSUBADD213PS = 810
        VFMSUBADDPD = 811
        VFMSUBADD231PD = 812
        VFMSUBADDPS = 813
        VFMSUBADD231PS = 814
        VFMSUBPD = 815
        VFMSUB231PD = 816
        VFMSUBPS = 817
        VFMSUB231PS = 818
        VFMSUBSD = 819
        VFMSUB213SD = 820
        VFMSUB132SD = 821
        VFMSUB231SD = 822
        VFMSUBSS = 823
        VFMSUB213SS = 824
        VFMSUB132SS = 825
        VFMSUB231SS = 826
        VFNMADD132PD = 827
        VFNMADD132PS = 828
        VFNMADD213PD = 829
        VFNMADD213PS = 830
        VFNMADDPD = 831
        VFNMADD231PD = 832
        VFNMADDPS = 833
        VFNMADD231PS = 834
        VFNMADDSD = 835
        VFNMADD213SD = 836
        VFNMADD132SD = 837
        VFNMADD231SD = 838
        VFNMADDSS = 839
        VFNMADD213SS = 840
        VFNMADD132SS = 841
        VFNMADD231SS = 842
        VFNMSUB132PD = 843
        VFNMSUB132PS = 844
        VFNMSUB213PD = 845
        VFNMSUB213PS = 846
        VFNMSUBPD = 847
        VFNMSUB231PD = 848
        VFNMSUBPS = 849
        VFNMSUB231PS = 850
        VFNMSUBSD = 851
        VFNMSUB213SD = 852
        VFNMSUB132SD = 853
        VFNMSUB231SD = 854
        VFNMSUBSS = 855
        VFNMSUB213SS = 856
        VFNMSUB132SS = 857
        VFNMSUB231SS = 858
        VFRCZPD = 859
        VFRCZPS = 860
        VFRCZSD = 861
        VFRCZSS = 862
        VORPD = 863
        VORPS = 864
        VXORPD = 865
        VXORPS = 866
        VGATHERDPD = 867
        VGATHERDPS = 868
        VGATHERPF0DPD = 869
        VGATHERPF0DPS = 870
        VGATHERPF0QPD = 871
        VGATHERPF0QPS = 872
        VGATHERPF1DPD = 873
        VGATHERPF1DPS = 874
        VGATHERPF1QPD = 875
        VGATHERPF1QPS = 876
        VGATHERQPD = 877
        VGATHERQPS = 878
        VHADDPD = 879
        VHADDPS = 880
        VHSUBPD = 881
        VHSUBPS = 882
        VINSERTF128 = 883
        VINSERTF32X4 = 884
        VINSERTF64X4 = 885
        VINSERTI128 = 886
        VINSERTI32X4 = 887
        VINSERTI64X4 = 888
        VINSERTPS = 889
        VLDDQU = 890
        VLDMXCSR = 891
        VMASKMOVDQU = 892
        VMASKMOVPD = 893
        VMASKMOVPS = 894
        VMAXPD = 895
        VMAXPS = 896
        VMAXSD = 897
        VMAXSS = 898
        VMCALL = 899
        VMCLEAR = 900
        VMFUNC = 901
        VMINPD = 902
        VMINPS = 903
        VMINSD = 904
        VMINSS = 905
        VMLAUNCH = 906
        VMLOAD = 907
        VMMCALL = 908
        VMOVQ = 909
        VMOVDDUP = 910
        VMOVD = 911
        VMOVDQA32 = 912
        VMOVDQA64 = 913
        VMOVDQA = 914
        VMOVDQU16 = 915
        VMOVDQU32 = 916
        VMOVDQU64 = 917
        VMOVDQU8 = 918
        VMOVDQU = 919
        VMOVHLPS = 920
        VMOVHPD = 921
        VMOVHPS = 922
        VMOVLHPS = 923
        VMOVLPD = 924
        VMOVLPS = 925
        VMOVMSKPD = 926
        VMOVMSKPS = 927
        VMOVNTDQA = 928
        VMOVNTDQ = 929
        VMOVNTPD = 930
        VMOVNTPS = 931
        VMOVSD = 932
        VMOVSHDUP = 933
        VMOVSLDUP = 934
        VMOVSS = 935
        VMOVUPD = 936
        VMOVUPS = 937
        VMPSADBW = 938
        VMPTRLD = 939
        VMPTRST = 940
        VMREAD = 941
        VMRESUME = 942
        VMRUN = 943
        VMSAVE = 944
        VMULPD = 945
        VMULPS = 946
        VMULSD = 947
        VMULSS = 948
        VMWRITE = 949
        VMXOFF = 950
        VMXON = 951
        VPABSB = 952
        VPABSD = 953
        VPABSQ = 954
        VPABSW = 955
        VPACKSSDW = 956
        VPACKSSWB = 957
        VPACKUSDW = 958
        VPACKUSWB = 959
        VPADDB = 960
        VPADDD = 961
        VPADDQ = 962
        VPADDSB = 963
        VPADDSW = 964
        VPADDUSB = 965
        VPADDUSW = 966
        VPADDW = 967
        VPALIGNR = 968
        VPANDD = 969
        VPANDND = 970
        VPANDNQ = 971
        VPANDN = 972
        VPANDQ = 973
        VPAND = 974
        VPAVGB = 975
        VPAVGW = 976
        VPBLENDD = 977
        VPBLENDMD = 978
        VPBLENDMQ = 979
        VPBLENDVB = 980
        VPBLENDW = 981
        VPBROADCASTB = 982
        VPBROADCASTD = 983
        VPBROADCASTMB2Q = 984
        VPBROADCASTMW2D = 985
        VPBROADCASTQ = 986
        VPBROADCASTW = 987
        VPCLMULQDQ = 988
        VPCMOV = 989
        VPCMP = 990
        VPCMPD = 991
        VPCMPEQB = 992
        VPCMPEQD = 993
        VPCMPEQQ = 994
        VPCMPEQW = 995
        VPCMPESTRI = 996
        VPCMPESTRM = 997
        VPCMPGTB = 998
        VPCMPGTD = 999
        VPCMPGTQ = 1000
        VPCMPGTW = 1001
        VPCMPISTRI = 1002
        VPCMPISTRM = 1003
        VPCMPQ = 1004
        VPCMPUD = 1005
        VPCMPUQ = 1006
        VPCOMB = 1007
        VPCOMD = 1008
        VPCOMQ = 1009
        VPCOMUB = 1010
        VPCOMUD = 1011
        VPCOMUQ = 1012
        VPCOMUW = 1013
        VPCOMW = 1014
        VPCONFLICTD = 1015
        VPCONFLICTQ = 1016
        VPERM2F128 = 1017
        VPERM2I128 = 1018
        VPERMD = 1019
        VPERMI2D = 1020
        VPERMI2PD = 1021
        VPERMI2PS = 1022
        VPERMI2Q = 1023
        VPERMIL2PD = 1024
        VPERMIL2PS = 1025
        VPERMILPD = 1026
        VPERMILPS = 1027
        VPERMPD = 1028
        VPERMPS = 1029
        VPERMQ = 1030
        VPERMT2D = 1031
        VPERMT2PD = 1032
        VPERMT2PS = 1033
        VPERMT2Q = 1034
        VPEXTRB = 1035
        VPEXTRD = 1036
        VPEXTRQ = 1037
        VPEXTRW = 1038
        VPGATHERDD = 1039
        VPGATHERDQ = 1040
        VPGATHERQD = 1041
        VPGATHERQQ = 1042
        VPHADDBD = 1043
        VPHADDBQ = 1044
        VPHADDBW = 1045
        VPHADDDQ = 1046
        VPHADDD = 1047
        VPHADDSW = 1048
        VPHADDUBD = 1049
        VPHADDUBQ = 1050
        VPHADDUBW = 1051
        VPHADDUDQ = 1052
        VPHADDUWD = 1053
        VPHADDUWQ = 1054
        VPHADDWD = 1055
        VPHADDWQ = 1056
        VPHADDW = 1057
        VPHMINPOSUW = 1058
        VPHSUBBW = 1059
        VPHSUBDQ = 1060
        VPHSUBD = 1061
        VPHSUBSW = 1062
        VPHSUBWD = 1063
        VPHSUBW = 1064
        VPINSRB = 1065
        VPINSRD = 1066
        VPINSRQ = 1067
        VPINSRW = 1068
        VPLZCNTD = 1069
        VPLZCNTQ = 1070
        VPMACSDD = 1071
        VPMACSDQH = 1072
        VPMACSDQL = 1073
        VPMACSSDD = 1074
        VPMACSSDQH = 1075
        VPMACSSDQL = 1076
        VPMACSSWD = 1077
        VPMACSSWW = 1078
        VPMACSWD = 1079
        VPMACSWW = 1080
        VPMADCSSWD = 1081
        VPMADCSWD = 1082
        VPMADDUBSW = 1083
        VPMADDWD = 1084
        VPMASKMOVD = 1085
        VPMASKMOVQ = 1086
        VPMAXSB = 1087
        VPMAXSD = 1088
        VPMAXSQ = 1089
        VPMAXSW = 1090
        VPMAXUB = 1091
        VPMAXUD = 1092
        VPMAXUQ = 1093
        VPMAXUW = 1094
        VPMINSB = 1095
        VPMINSD = 1096
        VPMINSQ = 1097
        VPMINSW = 1098
        VPMINUB = 1099
        VPMINUD = 1100
        VPMINUQ = 1101
        VPMINUW = 1102
        VPMOVDB = 1103
        VPMOVDW = 1104
        VPMOVMSKB = 1105
        VPMOVQB = 1106
        VPMOVQD = 1107
        VPMOVQW = 1108
        VPMOVSDB = 1109
        VPMOVSDW = 1110
        VPMOVSQB = 1111
        VPMOVSQD = 1112
        VPMOVSQW = 1113
        VPMOVSXBD = 1114
        VPMOVSXBQ = 1115
        VPMOVSXBW = 1116
        VPMOVSXDQ = 1117
        VPMOVSXWD = 1118
        VPMOVSXWQ = 1119
        VPMOVUSDB = 1120
        VPMOVUSDW = 1121
        VPMOVUSQB = 1122
        VPMOVUSQD = 1123
        VPMOVUSQW = 1124
        VPMOVZXBD = 1125
        VPMOVZXBQ = 1126
        VPMOVZXBW = 1127
        VPMOVZXDQ = 1128
        VPMOVZXWD = 1129
        VPMOVZXWQ = 1130
        VPMULDQ = 1131
        VPMULHRSW = 1132
        VPMULHUW = 1133
        VPMULHW = 1134
        VPMULLD = 1135
        VPMULLW = 1136
        VPMULUDQ = 1137
        VPORD = 1138
        VPORQ = 1139
        VPOR = 1140
        VPPERM = 1141
        VPROTB = 1142
        VPROTD = 1143
        VPROTQ = 1144
        VPROTW = 1145
        VPSADBW = 1146
        VPSCATTERDD = 1147
        VPSCATTERDQ = 1148
        VPSCATTERQD = 1149
        VPSCATTERQQ = 1150
        VPSHAB = 1151
        VPSHAD = 1152
        VPSHAQ = 1153
        VPSHAW = 1154
        VPSHLB = 1155
        VPSHLD = 1156
        VPSHLQ = 1157
        VPSHLW = 1158
        VPSHUFB = 1159
        VPSHUFD = 1160
        VPSHUFHW = 1161
        VPSHUFLW = 1162
        VPSIGNB = 1163
        VPSIGND = 1164
        VPSIGNW = 1165
        VPSLLDQ = 1166
        VPSLLD = 1167
        VPSLLQ = 1168
        VPSLLVD = 1169
        VPSLLVQ = 1170
        VPSLLW = 1171
        VPSRAD = 1172
        VPSRAQ = 1173
        VPSRAVD = 1174
        VPSRAVQ = 1175
        VPSRAW = 1176
        VPSRLDQ = 1177
        VPSRLD = 1178
        VPSRLQ = 1179
        VPSRLVD = 1180
        VPSRLVQ = 1181
        VPSRLW = 1182
        VPSUBB = 1183
        VPSUBD = 1184
        VPSUBQ = 1185
        VPSUBSB = 1186
        VPSUBSW = 1187
        VPSUBUSB = 1188
        VPSUBUSW = 1189
        VPSUBW = 1190
        VPTESTMD = 1191
        VPTESTMQ = 1192
        VPTESTNMD = 1193
        VPTESTNMQ = 1194
        VPTEST = 1195
        VPUNPCKHBW = 1196
        VPUNPCKHDQ = 1197
        VPUNPCKHQDQ = 1198
        VPUNPCKHWD = 1199
        VPUNPCKLBW = 1200
        VPUNPCKLDQ = 1201
        VPUNPCKLQDQ = 1202
        VPUNPCKLWD = 1203
        VPXORD = 1204
        VPXORQ = 1205
        VPXOR = 1206
        VRCP14PD = 1207
        VRCP14PS = 1208
        VRCP14SD = 1209
        VRCP14SS = 1210
        VRCP28PD = 1211
        VRCP28PS = 1212
        VRCP28SD = 1213
        VRCP28SS = 1214
        VRCPPS = 1215
        VRCPSS = 1216
        VRNDSCALEPD = 1217
        VRNDSCALEPS = 1218
        VRNDSCALESD = 1219
        VRNDSCALESS = 1220
        VROUNDPD = 1221
        VROUNDPS = 1222
        VROUNDSD = 1223
        VROUNDSS = 1224
        VRSQRT14PD = 1225
        VRSQRT14PS = 1226
        VRSQRT14SD = 1227
        VRSQRT14SS = 1228
        VRSQRT28PD = 1229
        VRSQRT28PS = 1230
        VRSQRT28SD = 1231
        VRSQRT28SS = 1232
        VRSQRTPS = 1233
        VRSQRTSS = 1234
        VSCATTERDPD = 1235
        VSCATTERDPS = 1236
        VSCATTERPF0DPD = 1237
        VSCATTERPF0DPS = 1238
        VSCATTERPF0QPD = 1239
        VSCATTERPF0QPS = 1240
        VSCATTERPF1DPD = 1241
        VSCATTERPF1DPS = 1242
        VSCATTERPF1QPD = 1243
        VSCATTERPF1QPS = 1244
        VSCATTERQPD = 1245
        VSCATTERQPS = 1246
        VSHUFPD = 1247
        VSHUFPS = 1248
        VSQRTPD = 1249
        VSQRTPS = 1250
        VSQRTSD = 1251
        VSQRTSS = 1252
        VSTMXCSR = 1253
        VSUBPD = 1254
        VSUBPS = 1255
        VSUBSD = 1256
        VSUBSS = 1257
        VTESTPD = 1258
        VTESTPS = 1259
        VUNPCKHPD = 1260
        VUNPCKHPS = 1261
        VUNPCKLPD = 1262
        VUNPCKLPS = 1263
        VZEROALL = 1264
        VZEROUPPER = 1265
        WAIT = 1266
        WBINVD = 1267
        WRFSBASE = 1268
        WRGSBASE = 1269
        WRMSR = 1270
        XABORT = 1271
        XACQUIRE = 1272
        XBEGIN = 1273
        XCHG = 1274
        FXCH = 1275
        XCRYPTCBC = 1276
        XCRYPTCFB = 1277
        XCRYPTCTR = 1278
        XCRYPTECB = 1279
        XCRYPTOFB = 1280
        XEND = 1281
        XGETBV = 1282
        XLATB = 1283
        XRELEASE = 1284
        XRSTOR = 1285
        XRSTOR64 = 1286
        XSAVE = 1287
        XSAVE64 = 1288
        XSAVEOPT = 1289
        XSAVEOPT64 = 1290
        XSETBV = 1291
        XSHA1 = 1292
        XSHA256 = 1293
        XSTORE = 1294
        XTEST = 1295
    class ARM32(IntEnum):
        ADC = 1296
        ADD = 1297
        ADR = 1298
        AESD = 1299
        AESE = 1300
        AESIMC = 1301
        AESMC = 1302
        AND = 1303
        BFC = 1304
        BFI = 1305
        BIC = 1306
        BKPT = 1307
        BL = 1308
        BLX = 1309
        BX = 1310
        BXJ = 1311
        B = 1312
        CDP = 1313
        CDP2 = 1314
        CLREX = 1315
        CLZ = 1316
        CMN = 1317
        CMP = 1318
        CPS = 1319
        CRC32B = 1320
        CRC32CB = 1321
        CRC32CH = 1322
        CRC32CW = 1323
        CRC32H = 1324
        CRC32W = 1325
        DBG = 1326
        DMB = 1327
        DSB = 1328
        EOR = 1329
        ERET = 1330
        VMOV = 1331
        FLDMDBX = 1332
        FLDMIAX = 1333
        VMRS = 1334
        FSTMDBX = 1335
        FSTMIAX = 1336
        HINT = 1337
        HLT = 1338
        HVC = 1339
        ISB = 1340
        LDA = 1341
        LDAB = 1342
        LDAEX = 1343
        LDAEXB = 1344
        LDAEXD = 1345
        LDAEXH = 1346
        LDAH = 1347
        LDC2L = 1348
        LDC2 = 1349
        LDCL = 1350
        LDC = 1351
        LDMDA = 1352
        LDMDB = 1353
        LDM = 1354
        LDMIB = 1355
        LDRBT = 1356
        LDRB = 1357
        LDRD = 1358
        LDREX = 1359
        LDREXB = 1360
        LDREXD = 1361
        LDREXH = 1362
        LDRH = 1363
        LDRHT = 1364
        LDRSB = 1365
        LDRSBT = 1366
        LDRSH = 1367
        LDRSHT = 1368
        LDRT = 1369
        LDR = 1370
        MCR = 1371
        MCR2 = 1372
        MCRR = 1373
        MCRR2 = 1374
        MLA = 1375
        MLS = 1376
        MOV = 1377
        MOVT = 1378
        MOVW = 1379
        MRC = 1380
        MRC2 = 1381
        MRRC = 1382
        MRRC2 = 1383
        MRS = 1384
        MSR = 1385
        MUL = 1386
        MVN = 1387
        ORR = 1388
        PKHBT = 1389
        PKHTB = 1390
        PLDW = 1391
        PLD = 1392
        PLI = 1393
        QADD = 1394
        QADD16 = 1395
        QADD8 = 1396
        QASX = 1397
        QDADD = 1398
        QDSUB = 1399
        QSAX = 1400
        QSUB = 1401
        QSUB16 = 1402
        QSUB8 = 1403
        RBIT = 1404
        REV = 1405
        REV16 = 1406
        REVSH = 1407
        RFEDA = 1408
        RFEDB = 1409
        RFEIA = 1410
        RFEIB = 1411
        RSB = 1412
        RSC = 1413
        SADD16 = 1414
        SADD8 = 1415
        SASX = 1416
        SBC = 1417
        SBFX = 1418
        SDIV = 1419
        SEL = 1420
        SETEND = 1421
        SHA1C = 1422
        SHA1H = 1423
        SHA1M = 1424
        SHA1P = 1425
        SHA1SU0 = 1426
        SHA1SU1 = 1427
        SHA256H = 1428
        SHA256H2 = 1429
        SHA256SU0 = 1430
        SHA256SU1 = 1431
        SHADD16 = 1432
        SHADD8 = 1433
        SHASX = 1434
        SHSAX = 1435
        SHSUB16 = 1436
        SHSUB8 = 1437
        SMC = 1438
        SMLABB = 1439
        SMLABT = 1440
        SMLAD = 1441
        SMLADX = 1442
        SMLAL = 1443
        SMLALBB = 1444
        SMLALBT = 1445
        SMLALD = 1446
        SMLALDX = 1447
        SMLALTB = 1448
        SMLALTT = 1449
        SMLATB = 1450
        SMLATT = 1451
        SMLAWB = 1452
        SMLAWT = 1453
        SMLSD = 1454
        SMLSDX = 1455
        SMLSLD = 1456
        SMLSLDX = 1457
        SMMLA = 1458
        SMMLAR = 1459
        SMMLS = 1460
        SMMLSR = 1461
        SMMUL = 1462
        SMMULR = 1463
        SMUAD = 1464
        SMUADX = 1465
        SMULBB = 1466
        SMULBT = 1467
        SMULL = 1468
        SMULTB = 1469
        SMULTT = 1470
        SMULWB = 1471
        SMULWT = 1472
        SMUSD = 1473
        SMUSDX = 1474
        SRSDA = 1475
        SRSDB = 1476
        SRSIA = 1477
        SRSIB = 1478
        SSAT = 1479
        SSAT16 = 1480
        SSAX = 1481
        SSUB16 = 1482
        SSUB8 = 1483
        STC2L = 1484
        STC2 = 1485
        STCL = 1486
        STC = 1487
        STL = 1488
        STLB = 1489
        STLEX = 1490
        STLEXB = 1491
        STLEXD = 1492
        STLEXH = 1493
        STLH = 1494
        STMDA = 1495
        STMDB = 1496
        STM = 1497
        STMIB = 1498
        STRBT = 1499
        STRB = 1500
        STRD = 1501
        STREX = 1502
        STREXB = 1503
        STREXD = 1504
        STREXH = 1505
        STRH = 1506
        STRHT = 1507
        STRT = 1508
        STR = 1509
        SUB = 1510
        SVC = 1511
        SWP = 1512
        SWPB = 1513
        SXTAB = 1514
        SXTAB16 = 1515
        SXTAH = 1516
        SXTB = 1517
        SXTB16 = 1518
        SXTH = 1519
        TEQ = 1520
        TRAP = 1521
        TST = 1522
        UADD16 = 1523
        UADD8 = 1524
        UASX = 1525
        UBFX = 1526
        UDF = 1527
        UDIV = 1528
        UHADD16 = 1529
        UHADD8 = 1530
        UHASX = 1531
        UHSAX = 1532
        UHSUB16 = 1533
        UHSUB8 = 1534
        UMAAL = 1535
        UMLAL = 1536
        UMULL = 1537
        UQADD16 = 1538
        UQADD8 = 1539
        UQASX = 1540
        UQSAX = 1541
        UQSUB16 = 1542
        UQSUB8 = 1543
        USAD8 = 1544
        USADA8 = 1545
        USAT = 1546
        USAT16 = 1547
        USAX = 1548
        USUB16 = 1549
        USUB8 = 1550
        UXTAB = 1551
        UXTAB16 = 1552
        UXTAH = 1553
        UXTB = 1554
        UXTB16 = 1555
        UXTH = 1556
        VABAL = 1557
        VABA = 1558
        VABDL = 1559
        VABD = 1560
        VABS = 1561
        VACGE = 1562
        VACGT = 1563
        VADD = 1564
        VADDHN = 1565
        VADDL = 1566
        VADDW = 1567
        VAND = 1568
        VBIC = 1569
        VBIF = 1570
        VBIT = 1571
        VBSL = 1572
        VCEQ = 1573
        VCGE = 1574
        VCGT = 1575
        VCLE = 1576
        VCLS = 1577
        VCLT = 1578
        VCLZ = 1579
        VCMP = 1580
        VCMPE = 1581
        VCNT = 1582
        VCVTA = 1583
        VCVTB = 1584
        VCVT = 1585
        VCVTM = 1586
        VCVTN = 1587
        VCVTP = 1588
        VCVTT = 1589
        VDIV = 1590
        VDUP = 1591
        VEOR = 1592
        VEXT = 1593
        VFMA = 1594
        VFMS = 1595
        VFNMA = 1596
        VFNMS = 1597
        VHADD = 1598
        VHSUB = 1599
        VLD1 = 1600
        VLD2 = 1601
        VLD3 = 1602
        VLD4 = 1603
        VLDMDB = 1604
        VLDMIA = 1605
        VLDR = 1606
        VMAXNM = 1607
        VMAX = 1608
        VMINNM = 1609
        VMIN = 1610
        VMLA = 1611
        VMLAL = 1612
        VMLS = 1613
        VMLSL = 1614
        VMOVL = 1615
        VMOVN = 1616
        VMSR = 1617
        VMUL = 1618
        VMULL = 1619
        VMVN = 1620
        VNEG = 1621
        VNMLA = 1622
        VNMLS = 1623
        VNMUL = 1624
        VORN = 1625
        VORR = 1626
        VPADAL = 1627
        VPADDL = 1628
        VPADD = 1629
        VPMAX = 1630
        VPMIN = 1631
        VQABS = 1632
        VQADD = 1633
        VQDMLAL = 1634
        VQDMLSL = 1635
        VQDMULH = 1636
        VQDMULL = 1637
        VQMOVUN = 1638
        VQMOVN = 1639
        VQNEG = 1640
        VQRDMULH = 1641
        VQRSHL = 1642
        VQRSHRN = 1643
        VQRSHRUN = 1644
        VQSHL = 1645
        VQSHLU = 1646
        VQSHRN = 1647
        VQSHRUN = 1648
        VQSUB = 1649
        VRADDHN = 1650
        VRECPE = 1651
        VRECPS = 1652
        VREV16 = 1653
        VREV32 = 1654
        VREV64 = 1655
        VRHADD = 1656
        VRINTA = 1657
        VRINTM = 1658
        VRINTN = 1659
        VRINTP = 1660
        VRINTR = 1661
        VRINTX = 1662
        VRINTZ = 1663
        VRSHL = 1664
        VRSHRN = 1665
        VRSHR = 1666
        VRSQRTE = 1667
        VRSQRTS = 1668
        VRSRA = 1669
        VRSUBHN = 1670
        VSELEQ = 1671
        VSELGE = 1672
        VSELGT = 1673
        VSELVS = 1674
        VSHLL = 1675
        VSHL = 1676
        VSHRN = 1677
        VSHR = 1678
        VSLI = 1679
        VSQRT = 1680
        VSRA = 1681
        VSRI = 1682
        VST1 = 1683
        VST2 = 1684
        VST3 = 1685
        VST4 = 1686
        VSTMDB = 1687
        VSTMIA = 1688
        VSTR = 1689
        VSUB = 1690
        VSUBHN = 1691
        VSUBL = 1692
        VSUBW = 1693
        VSWP = 1694
        VTBL = 1695
        VTBX = 1696
        VCVTR = 1697
        VTRN = 1698
        VTST = 1699
        VUZP = 1700
        VZIP = 1701
        ADDW = 1702
        ASR = 1703
        DCPS1 = 1704
        DCPS2 = 1705
        DCPS3 = 1706
        IT = 1707
        LSL = 1708
        LSR = 1709
        ORN = 1710
        ROR = 1711
        RRX = 1712
        SUBW = 1713
        TBB = 1714
        TBH = 1715
        CBNZ = 1716
        CBZ = 1717
        POP = 1718
        PUSH = 1719
        NOP = 1720
        YIELD = 1721
        WFE = 1722
        WFI = 1723
        SEV = 1724
        SEVL = 1725
        VPUSH = 1726
        VPOP = 1727
    class AARCH64(IntEnum):
        ABS = 1728
        ADC = 1729
        ADD = 1730
        ADDHN = 1731
        ADDHN2 = 1732
        ADDP = 1733
        ADDV = 1734
        ADR = 1735
        ADRP = 1736
        AESD = 1737
        AESE = 1738
        AESIMC = 1739
        AESMC = 1740
        AND = 1741
        ASR = 1742
        AT = 1743
        B = 1744
        BFI = 1745
        BFM = 1746
        BFXIL = 1747
        BIC = 1748
        BIF = 1749
        BIT = 1750
        BL = 1751
        BLR = 1752
        BR = 1753
        BRK = 1754
        BSL = 1755
        CBNZ = 1756
        CBZ = 1757
        CCMN = 1758
        CCMP = 1759
        CINC = 1760
        CINV = 1761
        CLREX = 1762
        CLS = 1763
        CLZ = 1764
        CMEQ = 1765
        CMGE = 1766
        CMGT = 1767
        CMHI = 1768
        CMHS = 1769
        CMLE = 1770
        CMLT = 1771
        CMN = 1772
        CMP = 1773
        CMTST = 1774
        CNEG = 1775
        CNT = 1776
        CRC32B = 1777
        CRC32CB = 1778
        CRC32CH = 1779
        CRC32CW = 1780
        CRC32CX = 1781
        CRC32H = 1782
        CRC32W = 1783
        CRC32X = 1784
        CSEL = 1785
        CSET = 1786
        CSETM = 1787
        CSINC = 1788
        CSINV = 1789
        CSNEG = 1790
        DC = 1791
        DCPS1 = 1792
        DCPS2 = 1793
        DCPS3 = 1794
        DMB = 1795
        DRPS = 1796
        DSB = 1797
        DUP = 1798
        EON = 1799
        EOR = 1800
        ERET = 1801
        EXT = 1802
        EXTR = 1803
        FABD = 1804
        FABS = 1805
        FACGE = 1806
        FACGT = 1807
        FADD = 1808
        FADDP = 1809
        FCCMP = 1810
        FCCMPE = 1811
        FCMEQ = 1812
        FCMGE = 1813
        FCMGT = 1814
        FCMLE = 1815
        FCMLT = 1816
        FCMP = 1817
        FCMPE = 1818
        FCSEL = 1819
        FCVT = 1820
        FCVTAS = 1821
        FCVTAU = 1822
        FCVTL = 1823
        FCVTL2 = 1824
        FCVTMS = 1825
        FCVTMU = 1826
        FCVTN = 1827
        FCVTN2 = 1828
        FCVTNS = 1829
        FCVTNU = 1830
        FCVTPS = 1831
        FCVTPU = 1832
        FCVTXN = 1833
        FCVTXN2 = 1834
        FCVTZS = 1835
        FCVTZU = 1836
        FDIV = 1837
        FMADD = 1838
        FMAX = 1839
        FMAXNM = 1840
        FMAXNMP = 1841
        FMAXNMV = 1842
        FMAXP = 1843
        FMAXV = 1844
        FMIN = 1845
        FMINNM = 1846
        FMINNMP = 1847
        FMINNMV = 1848
        FMINP = 1849
        FMINV = 1850
        FMLA = 1851
        FMLS = 1852
        FMOV = 1853
        FMSUB = 1854
        FMUL = 1855
        FMULX = 1856
        FNEG = 1857
        FNMADD = 1858
        FNMSUB = 1859
        FNMUL = 1860
        FRECPE = 1861
        FRECPS = 1862
        FRECPX = 1863
        FRINTA = 1864
        FRINTI = 1865
        FRINTM = 1866
        FRINTN = 1867
        FRINTP = 1868
        FRINTX = 1869
        FRINTZ = 1870
        FRSQRTE = 1871
        FRSQRTS = 1872
        FSQRT = 1873
        FSUB = 1874
        HINT = 1875
        HLT = 1876
        HVC = 1877
        IC = 1878
        INS = 1879
        ISB = 1880
        LD1 = 1881
        LD1R = 1882
        LD2 = 1883
        LD2R = 1884
        LD3 = 1885
        LD3R = 1886
        LD4 = 1887
        LD4R = 1888
        LDAR = 1889
        LDARB = 1890
        LDARH = 1891
        LDAXP = 1892
        LDAXR = 1893
        LDAXRB = 1894
        LDAXRH = 1895
        LDNP = 1896
        LDP = 1897
        LDPSW = 1898
        LDR = 1899
        LDRB = 1900
        LDRH = 1901
        LDRSB = 1902
        LDRSH = 1903
        LDRSW = 1904
        LDTR = 1905
        LDTRB = 1906
        LDTRH = 1907
        LDTRSB = 1908
        LDTRSH = 1909
        LDTRSW = 1910
        LDUR = 1911
        LDURB = 1912
        LDURH = 1913
        LDURSB = 1914
        LDURSH = 1915
        LDURSW = 1916
        LDXP = 1917
        LDXR = 1918
        LDXRB = 1919
        LDXRH = 1920
        LSL = 1921
        LSR = 1922
        MADD = 1923
        MLA = 1924
        MLS = 1925
        MNEG = 1926
        MOV = 1927
        MOVI = 1928
        MOVK = 1929
        MOVN = 1930
        MOVZ = 1931
        MRS = 1932
        MSR = 1933
        MSUB = 1934
        MUL = 1935
        MVN = 1936
        MVNI = 1937
        NEG = 1938
        NGC = 1939
        NOP = 1940
        NOT = 1941
        ORN = 1942
        ORR = 1943
        PMUL = 1944
        PMULL = 1945
        PMULL2 = 1946
        PRFM = 1947
        PRFUM = 1948
        RADDHN = 1949
        RADDHN2 = 1950
        RBIT = 1951
        RET = 1952
        REV = 1953
        REV16 = 1954
        REV32 = 1955
        REV64 = 1956
        ROR = 1957
        RSHRN = 1958
        RSHRN2 = 1959
        RSUBHN = 1960
        RSUBHN2 = 1961
        SABA = 1962
        SABAL = 1963
        SABAL2 = 1964
        SABD = 1965
        SABDL = 1966
        SABDL2 = 1967
        SADALP = 1968
        SADDL = 1969
        SADDL2 = 1970
        SADDLP = 1971
        SADDLV = 1972
        SADDW = 1973
        SADDW2 = 1974
        SBC = 1975
        SBFIZ = 1976
        SBFM = 1977
        SBFX = 1978
        SCVTF = 1979
        SDIV = 1980
        SEV = 1981
        SEVL = 1982
        SHA1C = 1983
        SHA1H = 1984
        SHA1M = 1985
        SHA1P = 1986
        SHA1SU0 = 1987
        SHA1SU1 = 1988
        SHA256H = 1989
        SHA256H2 = 1990
        SHA256SU0 = 1991
        SHA256SU1 = 1992
        SHADD = 1993
        SHL = 1994
        SHLL = 1995
        SHLL2 = 1996
        SHRN = 1997
        SHRN2 = 1998
        SHSUB = 1999
        SLI = 2000
        SMADDL = 2001
        SMAX = 2002
        SMAXP = 2003
        SMAXV = 2004
        SMC = 2005
        SMIN = 2006
        SMINP = 2007
        SMINV = 2008
        SMLAL = 2009
        SMLAL2 = 2010
        SMLSL = 2011
        SMLSL2 = 2012
        SMNEGL = 2013
        SMOV = 2014
        SMSUBL = 2015
        SMULH = 2016
        SMULL = 2017
        SMULL2 = 2018
        SQABS = 2019
        SQADD = 2020
        SQDMLAL = 2021
        SQDMLAL2 = 2022
        SQDMLSL = 2023
        SQDMLSL2 = 2024
        SQDMULH = 2025
        SQDMULL = 2026
        SQDMULL2 = 2027
        SQNEG = 2028
        SQRDMULH = 2029
        SQRSHL = 2030
        SQRSHRN = 2031
        SQRSHRN2 = 2032
        SQRSHRUN = 2033
        SQRSHRUN2 = 2034
        SQSHL = 2035
        SQSHLU = 2036
        SQSHRN = 2037
        SQSHRN2 = 2038
        SQSHRUN = 2039
        SQSHRUN2 = 2040
        SQSUB = 2041
        SQXTN = 2042
        SQXTN2 = 2043
        SQXTUN = 2044
        SQXTUN2 = 2045
        SRHADD = 2046
        SRI = 2047
        SRSHL = 2048
        SRSHR = 2049
        SRSRA = 2050
        SSHL = 2051
        SSHLL = 2052
        SSHLL2 = 2053
        SSHR = 2054
        SSRA = 2055
        SSUBL = 2056
        SSUBL2 = 2057
        SSUBW = 2058
        SSUBW2 = 2059
        ST1 = 2060
        ST2 = 2061
        ST3 = 2062
        ST4 = 2063
        STLR = 2064
        STLRB = 2065
        STLRH = 2066
        STLXP = 2067
        STLXR = 2068
        STLXRB = 2069
        STLXRH = 2070
        STNP = 2071
        STP = 2072
        STR = 2073
        STRB = 2074
        STRH = 2075
        STTR = 2076
        STTRB = 2077
        STTRH = 2078
        STUR = 2079
        STURB = 2080
        STURH = 2081
        STXP = 2082
        STXR = 2083
        STXRB = 2084
        STXRH = 2085
        SUB = 2086
        SUBHN = 2087
        SUBHN2 = 2088
        SUQADD = 2089
        SVC = 2090
        SXTB = 2091
        SXTH = 2092
        SXTW = 2093
        SYS = 2094
        SYSL = 2095
        TBL = 2096
        TBNZ = 2097
        TBX = 2098
        TBZ = 2099
        TLBI = 2100
        TRN1 = 2101
        TRN2 = 2102
        TST = 2103
        UABA = 2104
        UABAL = 2105
        UABAL2 = 2106
        UABD = 2107
        UABDL = 2108
        UABDL2 = 2109
        UADALP = 2110
        UADDL = 2111
        UADDL2 = 2112
        UADDLP = 2113
        UADDLV = 2114
        UADDW = 2115
        UADDW2 = 2116
        UBFIZ = 2117
        UBFM = 2118
        UBFX = 2119
        UCVTF = 2120
        UDIV = 2121
        UHADD = 2122
        UHSUB = 2123
        UMADDL = 2124
        UMAX = 2125
        UMAXP = 2126
        UMAXV = 2127
        UMIN = 2128
        UMINP = 2129
        UMINV = 2130
        UMLAL = 2131
        UMLAL2 = 2132
        UMLSL = 2133
        UMLSL2 = 2134
        UMNEGL = 2135
        UMOV = 2136
        UMSUBL = 2137
        UMULH = 2138
        UMULL = 2139
        UMULL2 = 2140
        UQADD = 2141
        UQRSHL = 2142
        UQRSHRN = 2143
        UQRSHRN2 = 2144
        UQSHL = 2145
        UQSHRN = 2146
        UQSHRN2 = 2147
        UQSUB = 2148
        UQXTN = 2149
        UQXTN2 = 2150
        URECPE = 2151
        URHADD = 2152
        URSHL = 2153
        URSHR = 2154
        URSQRTE = 2155
        URSRA = 2156
        USHL = 2157
        USHLL = 2158
        USHLL2 = 2159
        USHR = 2160
        USQADD = 2161
        USRA = 2162
        USUBL = 2163
        USUBL2 = 2164
        USUBW = 2165
        USUBW2 = 2166
        UXTB = 2167
        UXTH = 2168
        UXTW = 2169
        UZP1 = 2170
        UZP2 = 2171
        WFE = 2172
        WFI = 2173
        XTN = 2174
        XTN2 = 2175
        YIELD = 2176
        ZIP1 = 2177
        ZIP2 = 2178
    class RV64(IntEnum):
        ADD = 2179
        ADDI = 2180
        ADDIW = 2181
        ADDW = 2182
        AND = 2183
        ANDI = 2184
        AUIPC = 2185
        BEQ = 2186
        BGE = 2187
        BGEU = 2188
        BLT = 2189
        BLTU = 2190
        BNE = 2191
        C_ADD = 2192
        C_ADDI = 2193
        C_ADDI16SP = 2194
        C_ADDI4SPN = 2195
        C_ADDIW = 2196
        C_ADDW = 2197
        C_AND = 2198
        C_ANDI = 2199
        C_BEQZ = 2200
        C_BNEZ = 2201
        C_J = 2202
        C_JALR = 2203
        C_JR = 2204
        C_LD = 2205
        C_LDSP = 2206
        C_LI = 2207
        C_LUI = 2208
        C_LW = 2209
        C_LWSP = 2210
        C_MV = 2211
        C_NOP = 2212
        C_OR = 2213
        C_SD = 2214
        C_SDSP = 2215
        C_SLLI = 2216
        C_SRAI = 2217
        C_SRLI = 2218
        C_SUB = 2219
        C_SUBW = 2220
        C_SW = 2221
        C_SWSP = 2222
        C_XOR = 2223
        DIV = 2224
        DIVU = 2225
        DIVUW = 2226
        DIVW = 2227
        JAL = 2228
        JALR = 2229
        LB = 2230
        LBU = 2231
        LD = 2232
        LH = 2233
        LHU = 2234
        LUI = 2235
        LW = 2236
        LWU = 2237
        MUL = 2238
        MULH = 2239
        MULHSU = 2240
        MULHU = 2241
        MULW = 2242
        OR = 2243
        ORI = 2244
        REM = 2245
        REMU = 2246
        REMUW = 2247
        REMW = 2248
        SB = 2249
        SD = 2250
        SH = 2251
        SLL = 2252
        SLLI = 2253
        SLLIW = 2254
        SLLW = 2255
        SLT = 2256
        SLTI = 2257
        SLTIU = 2258
        SLTU = 2259
        SRA = 2260
        SRAI = 2261
        SRAIW = 2262
        SRAW = 2263
        SRL = 2264
        SRLI = 2265
        SRLIW = 2266
        SRLW = 2267
        SUB = 2268
        SUBW = 2269
        SW = 2270
        XOR = 2271
        XORI = 2272
    class RV32(IntEnum):
        ADD = 2273
        ADDI = 2274
        AND = 2275
        ANDI = 2276
        AUIPC = 2277
        BEQ = 2278
        BGE = 2279
        BGEU = 2280
        BLT = 2281
        BLTU = 2282
        BNE = 2283
        C_ADD = 2284
        C_ADDI = 2285
        C_ADDI16SP = 2286
        C_ADDI4SPN = 2287
        C_AND = 2288
        C_ANDI = 2289
        C_BEQZ = 2290
        C_BNEZ = 2291
        C_J = 2292
        C_JAL = 2293
        C_JALR = 2294
        C_JR = 2295
        C_LI = 2296
        C_LUI = 2297
        C_LW = 2298
        C_LWSP = 2299
        C_MV = 2300
        C_NOP = 2301
        C_OR = 2302
        C_SLLI = 2303
        C_SRAI = 2304
        C_SRLI = 2305
        C_SUB = 2306
        C_SW = 2307
        C_SWSP = 2308
        C_XOR = 2309
        DIV = 2310
        DIVU = 2311
        JAL = 2312
        JALR = 2313
        LB = 2314
        LBU = 2315
        LD = 2316
        LH = 2317
        LHU = 2318
        LUI = 2319
        LW = 2320
        MUL = 2321
        MULH = 2322
        MULHS = 2323
        MULHU = 2324
        OR = 2325
        ORI = 2326
        REM = 2327
        REMU = 2328
        SB = 2329
        SH = 2330
        SLL = 2331
        SLLI = 2332
        SLT = 2333
        SLTI = 2334
        SLTIU = 2335
        SLTU = 2336
        SRA = 2337
        SRAI = 2338
        SRL = 2339
        SRLI = 2340
        SUB = 2341
        SW = 2342
        XOR = 2343
        XORI = 2344

class ARCH(IntEnum):
    AARCH64 = 1
    ARM32 = 2
    RV32 = 3
    RV64 = 4
    X86 = 5
    X86_64 = 6

class VERSION(IntEnum):
    BUILD = 1
    MAJOR = 2
    MINOR = 3
    BITWUZLA_INTERFACE = 4
    LLVM_INTERFACE = 5
    Z3_INTERFACE = 6

class EXTEND(IntEnum):
    pass
    class ARM(IntEnum):
        INVALID = 1
        UXTB = 2
        UXTH = 3
        UXTW = 4
        UXTX = 5
        SXTB = 6
        SXTH = 7
        SXTW = 8
        SXTX = 9

raise ImportError
