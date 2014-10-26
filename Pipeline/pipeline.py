import sys
import shlex
import os


def debug_redirect():
    if 'PYCHARM_HOSTED' in os.environ.keys():
        sys.stdin = open("input2.txt", 'r')
    parser = shlex.shlex(sys.stdin)
    parser.whitespace_split = True
    return parser


def parse_inputs(parser):
    n = int(parser.get_token())
    m = [[None for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            x = int(parser.get_token())
            m[r][c] = x
    return n, m


def pathfinder(table, cell, n, burned):
    row, col = cell
    burned.append(cell)
    if col == n-1:
        # last column, we're done
        yield [cell]
    else:
        # move right
        ncell = (row, col+1)
        if not ncell in burned:
            for path in pathfinder(table, ncell, n, burned[:]):
                yield path + [cell]
        # skip doing this on the first column, it's silly
        if col > 0:
            # move up
            if row < n-1:
                ncell = (row+1, col)
                if not ncell in burned:
                    for path in pathfinder(table, ncell, n, burned[:]):
                        yield path + [cell]
            # move down
            if row > 0:
                ncell = (row-1, col)
                if not ncell in burned:
                    for path in pathfinder(table, ncell, n, burned[:]):
                        yield path + [cell]


def cost(path, table):
    c = 0
    for row, col in path:
        c += table[row][col]
    return c


def main():
    parser = debug_redirect()
    n, m = parse_inputs(parser)
    g = n * n + 2
    mpath = None
    mcost = sys.maxint
    for r in range(n):
        for path in pathfinder(m, (r, 0), n, []):
            ccost = cost(path, m)
            if (mpath is None) or (ccost < mcost):
                mcost = ccost
                mpath = path
    print cost(mpath, m)


if "__main__" == __name__:
    main()