import sys
import shlex
import os


DENSITY = {
    '-': 0,
    'L': 1,
    'M': 2,
    'H': 3}


def neighbors(i, j, n, m):
    v = [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]
    for i in range(3, -1, -1):
        x, y = v[i]
        if 0 < x >= n or 0 < y >= m:
            del(v[i])
    return v


def setup():
    if 'PYCHARM_HOSTED' in os.environ.keys():
        sys.stdin = open("input2.txt", 'r')
    parser = shlex.shlex(sys.stdin)
    parser.whitespace += '*'
    parser.whitespace_split = True
    return parser


def parse(parser):
    n = int(parser.get_token())
    m = int(parser.get_token())
    shops = [[0 for _ in range(m)] for _ in range(n)]
    income = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(7)]

    for i in range(n):
        for j in range(m):
            x = parser.get_token()
            try:
                shops[i][j] = DENSITY[x]
            except KeyError:
                shops[i][j] = 0

    for k in range(7):
        day = parser.get_token()
        for i in range(n):
            for j in range(m):
                p = int(parser.get_token())
                c = shops[i][j]
                if c == 3:
                    income[k][i][j] = 0
                    if p >= 5:
                        for x, y in neighbors(i, j, n, m):
                            income[k][x][y] += 1
                else:
                    income[k][i][j] += p / (c + 1.0)
        for i in range(n):
            for j in range(m):
                income[k][i][j] = max(0, income[k][i][j] - 20)
    return n, m, shops, income


def optimal(n, m, income):
    best = 0
    cell = (-2, -2)
    for i in range(n):
        for j in range(m):
            w = [income[k][i][j] for k in range(7)]
            t = sum(w)
            if t > best:
                best = t
                cell = (i, j)   # Your issue arises from this definition of cell.
                                # The cell is determined by the for loops rather than t's coords.
    return cell


def main():
    parser = setup()
    n, m, shops, income = parse(parser)
    y, x = optimal(n, m, income)
    sys.stdout.write("{0} {1}".format(x+1, y+1))


if "__main__" == __name__:
    main()