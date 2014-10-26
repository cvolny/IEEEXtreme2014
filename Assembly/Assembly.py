import re
import sys
import fileinput
import os
import operator
from collections import OrderedDict, deque


DEREF_PATTERN = re.compile("\(([0-9A-F]+)\)")
LITER_PATTERN = re.compile("#([0-9A-F]+)")
OPS_BINARY = {
    'ADD':  operator.add,
    'SUB':  operator.sub,
    'OR': operator.or_,
    'AND': operator.and_,
    'XOR': operator.xor}
OPS_BRANCH = {
    'BEQ': operator.eq,
    'BNE': operator.ne,
    'BGT': operator.gt,
    'BLT': operator.lt,
    'BGE': operator.ge,
    'BLE': operator.le}


def setup():
    if 'PYCHARM_HOSTED' in os.environ.keys():
        sys.stdin = open("input2.txt", 'r')
        #sys.stdout = open("output1.txt", 'wc')
    return fileinput.input()


def parse(parser):
    cmds = []
    labels = {}
    for line in parser:
        line = ' '.join(line.split())
        if fileinput.isfirstline():
            n = int(line, 16)
        else:
            tokens = line.strip().split(" ")
            if 3 == len(tokens):
                labels[tokens[0]] = parser.lineno() - 2
                del(tokens[0])
            operation, arguments = tokens
            cmds.append((operation, arguments))
    return n, cmds, labels


def hexer(y):
    return int(y, 16)


def argument_parse(memory, token, unsafe=False):
    if DEREF_PATTERN.match(token):
        return memory[hexer(token[1:-1])]
    if LITER_PATTERN.match(token):
        return hexer(token[1:])
    if unsafe:
        return memory[hexer(token)]
    return hexer(token)


def interpret(memsize, program, labels):
    argval = lambda y, unsafe=False: argument_parse(memory, y, unsafe)
    cmpres = 0
    memory = [0 for _ in range(memsize+1)]
    instructions = deque(program)
    while len(instructions) > 0:
        op, arg = instructions.popleft()
        op = op.upper()
        args = arg.split(",")
        if 2 == len(args):
            left, right = args
        else:
            left, right = args[0], args[0]

        if "PRINT" == op:
            print " ".join([format(memory[x], '02X') for x in range(hexer(left), hexer(right)+1)])
        elif "MOVE" == op:
            memory[argval(right)] = argval(left, unsafe=True)
        elif "COMP" == op:
            cmpres = cmp(argval(left, unsafe=True), argval(right, unsafe=True))
        elif op in OPS_BINARY.keys():
            memory[argval(right)] = OPS_BINARY[op](argval(right, unsafe=True), argval(left, unsafe=True)) % 0x100
        elif op in OPS_BRANCH.keys():
            if OPS_BRANCH[op](cmpres, 0):
                instructions = deque(program[labels[arg]:])


def main():
    parser = setup()
    n, program, labels = parse(parser)
    interpret(n, program, labels)


if "__main__" == __name__:
    main()