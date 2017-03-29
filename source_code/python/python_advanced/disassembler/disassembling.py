import dis
from functools import reduce

def add(*arg):
    return reduce(lambda a, b: a + b, arg)

dis.dis(add)

bytecode = dis.Bytecode(add)

for instruction in bytecode:
    print(instruction.opname)


