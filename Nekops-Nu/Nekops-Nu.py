import sys
import shlex
import os


PADDING = "."


def setup():
    if 'PYCHARM_HOSTED' in os.environ.keys():
        sys.stdin = open("input1.txt", 'r')
        #sys.stdout = open("output1.txt", 'wc')
    parser = shlex.shlex(sys.stdin)
    parser.whitespace_split = True
    return parser


def parse(parser):
    k = int(parser.get_token())
    v = [int(x) for x in parser]
    return k, v


def nekops_nu(v):
    n = []
    c = 1
    p = v[0]
    for x in v[1:]:
        if x == p:
            c += 1
        else:
            n.extend([c, p])
            p = x
            c = 1
    n.extend([c, p])
    return n


def record(resultset, sequence):
    strseq = " ".join(str(x) for x in sequence)
    resultset.append(strseq)
    return len(strseq)


def main():
    parser = setup()
    r = []
    k, v = parse(parser)
    m = record(r, v)
    for i in range(k):
        v = nekops_nu(v)
        l = record(r, v)
        m = l if l > m else m

    for s in r:
        d = m - len(s)
        p = d / 2
        b = d - p
        print PADDING*b + s + PADDING*p
    print len(v)


if "__main__" == __name__:
    main()