import sys
import os
import fileinput
from collections import defaultdict
from operator import itemgetter


CLASS_ORDER = ('Intelligence', 'Strength', 'Agility')
CLASS_ORDER_SORT = CLASS_ORDER[::-1]


def setup():
    if 'PYCHARM_HOSTED' in os.environ.keys():
        sys.stdin = open("input2.txt", 'r')
    parser = fileinput.input()
    return parser


def rank(i, win, loss):
    return (win / (loss+win)) * i


def parse(parser):
    v = []
    for line in parser:
        if fileinput.isfirstline():
            n, m = map(int, line.split())
        else:
            args = line.rstrip().split(",")
            name, stat, winloss = args
            win, loss = map(float, winloss.split(":"))
            r = rank(parser.lineno() - 1, win, loss)
            c = CLASS_ORDER_SORT.index(stat)
            v.append({'name': name, 'stat': stat, 'win': win, 'loss': loss, 'rank': r, 'class_rank': c})
    return n, m, v


def main():
    parser = setup()
    n, m, v = parse(parser)
    v.sort(key=itemgetter('rank', 'class_rank'), reverse=True)
    pick = v[:m]
    counts = defaultdict(int)
    for x in pick:
        counts[x['stat']] += 1
        print(x['name'])
    print
    print "This set of heroes:"
    for stat in CLASS_ORDER:
        p = counts[stat] / float(m) * 100
        print "Contains {percent:0.2f} percentage of {stat}".format(percent=p, stat=stat)


if "__main__" == __name__:
    main()