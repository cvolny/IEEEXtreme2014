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
    m = int(parser.get_token())
    d = {}
    for x in range(1, n+1):
        d[x] = []
    for i in range(m):
        prereq = int(parser.get_token())
        course = int(parser.get_token())
        d[course].append(prereq)
    p = []
    while not parser.eof:
        try:
            x = int(parser.get_token())
            p.append(x)
        except ValueError:
            break
    return n, m, d, p


def check_plan(d, p):
    burn = []
    for x in p:
        burn.append(x)
        for y in d[x]:
            if not y in burn:
                return False
    return True


def main():
    parser = setup()
    n, m, d, p = parse(parser)
    print "YES" if check_plan(d, p) else "NO"


if "__main__" == __name__:
    main()