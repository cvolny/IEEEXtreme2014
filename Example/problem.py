import sys
import shlex
import os


def setup():
    if 'PYCHARM_HOSTED' in os.environ.keys():
        sys.stdin = open("input1.txt", 'r')
        #sys.stdout = open("output1.txt", 'wc')
    parser = shlex.shlex(sys.stdin)
    parser.whitespace_split = True
    return parser


def parse(parser):
    n = int(parser.get_token())
    return n


def main():
    parser = setup()
    n = parse(parser)


if "__main__" == __name__:
    main()