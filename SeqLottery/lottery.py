import sys
import shlex
import os


def setup():
    if 'PYCHARM_HOSTED' in os.environ.keys():
        sys.stdin = open("input1.txt", 'r')
    parser = shlex.shlex(sys.stdin)
    parser.whitespace_split = True
    return parser


def parse(parser):
    start = int(parser.get_token())
    final = int(parser.get_token())
    index = int(parser.get_token())
    count = int(parser.get_token())
    ivals = [None]*count
    for i in range(count):
        ivals[i] = parser.get_token()
    return start, final, index, count, ivals


def generate_from_sequence(v, start, final):
    for i in range(start, final+1):
        r = generate_from_sequence_helper(i, v)
        if r:
            yield r


def generate_from_sequence_helper(i, v):
    s = str(i)
    for x in v:
        if x in s:
            return i
    return False


def main():
    parser = setup()
    start, final, index, count, ivals = parse(parser)
    i = 1
    for x in generate_from_sequence(ivals, start, final):
        if i == index:
            print x
            exit()
        i += 1
    print "DOES NOT EXIST"


if "__main__" == __name__:
    main()