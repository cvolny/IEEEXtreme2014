import sys
import shlex
import os
from operator import itemgetter


def setup():
    if 'PYCHARM_HOSTED' in os.environ.keys():
        sys.stdin = open("input2.txt", 'r')
        #sys.stdout = open("output1.txt", 'wc')
    parser = shlex.shlex(sys.stdin)
    parser.whitespace += ","
    parser.whitespace_split = True
    return parser


def parse(parser):
    n = int(parser.get_token())
    m = int(parser.get_token())
    v = []
    while True:
        label = parser.get_token()
        if "END" == label:
            break
        count = int(parser.get_token())
        value = float(parser.get_token())
        ratio = value / count
        v.append({'label': label, 'ratio': ratio, 'count': count, 'value': value})
    return n, m, v


def determine_load(capacity, items):
    r = capacity
    v = []
    for x in items:
        c = min(r, x['count'])
        r -= c
        x['count'] -= c
        if c:
            v.append({'label': x['label'], 'count': c, 'value': x['ratio'] * c})
        if r == 0:
            break
    return v




def main():
    parser = setup()
    robbers, capacity, items = parse(parser)
    items.sort(key=itemgetter('ratio'), reverse=True)
    d = {}
    x = determine_load(capacity * robbers, items)
    stolen = sorted(x, key=itemgetter('label'))
    for x in stolen:
        print "{label},{count:d},{value:0.0f}".format(**x)
    count = sum([row['count'] for row in stolen])
    value = sum([row['value'] for row in stolen])
    share = robbers / value
    print "{count:d},{value:0.0f}".format(count=count, value=value)
    print "Each robber gets: {share:0.2f}".format(share=share)


if "__main__" == __name__:
    main()