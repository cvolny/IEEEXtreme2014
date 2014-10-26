import sys
import shlex
import os


CAL_BASE = 270
CAL_TOPS = {'Anchovies': 50,
            'Artichoke': 60,
            'Bacon': 92,
            'Broccoli': 24,
            'Cheese': 80,
            'Chicken': 30,
            'Feta': 99,
            'Garlic': 8,
            'Ham': 46,
            'Jalapeno': 5,
            'Meatballs': 120,
            'Mushrooms': 11,
            'Olives': 25,
            'Onions': 11,
            'Pepperoni': 80,
            'Peppers': 6,
            'Pineapple': 21,
            'Ricotta': 108,
            'Sausage': 115,
            'Spinach': 18,
            'Tomatoes': 14}


def test_lookup():
    assert toppings("Anchovies") == 50
    assert toppings("Artichoke") == 60
    assert toppings("Bacon") == 92
    assert toppings("Broccoli") == 24
    assert toppings("Cheese") == 80
    assert toppings("Chicken") == 30
    assert toppings("Feta") == 99
    assert toppings("Garlic") == 8
    assert toppings("Ham") == 46
    assert toppings("Jalapeno") == 5
    assert toppings("Meatballs") == 120
    assert toppings("Mushrooms") == 11
    assert toppings("Olives") == 25
    assert toppings("Onions") == 11
    assert toppings("Pepperoni") == 80
    assert toppings("Peppers") == 6
    assert toppings("Pineapple") == 21
    assert toppings("Ricotta") == 108
    assert toppings("Sausage") == 115
    assert toppings("Spinach") == 18
    assert toppings("Tomatoes") == 14


def setup():
    if 'PYCHARM_HOSTED' in os.environ.keys():
        sys.stdin = open("input1.txt", 'r')
        test_lookup()
        #sys.stdout = open("output1.txt", 'wc')
    parser = shlex.shlex(sys.stdin)
    parser.whitespace_split = True
    return parser


def parse(parser):
    n = int(parser.get_token())
    v = []
    for i in range(n):
        c = int(parser.get_token())
        t = parser.get_token().split(",")
        v.append((c, t))
    return n, v


def toppings(name):
    return CAL_TOPS[name]


def main():
    parser = setup()
    n, v = parse(parser)
    cals = sum([c * (CAL_BASE + sum([toppings(x) for x in t])) for c, t in v])
    print "The total calorie intake is {0}".format(cals)


if "__main__" == __name__:
    main()