from collections import defaultdict
from operator import mul
from functools import reduce

with open('input.txt') as fp:
    head, yourticket, neartickets = fp.read().split('\n\n')
    head, yourticket, neartickets = head.splitlines(), yourticket.splitlines(), neartickets.splitlines()

    data = {}
    for line in head:
        name, ranges = line.split(': ')
        r1, r2 = ranges.split(' or ')
        a, b = r1.split('-')
        c, d = r2.split('-')
        a, b, c, d = int(a), int(b), int(c), int(d)
        data[name] = {*range(a, b + 1), *range(c, d + 1)}
    
    yourticket = [int(i) for i in yourticket[1].split(',')]
    neartickets = [[int(i) for i in line.split(',')] for line in neartickets[1:]]

    all_values = {a for b in data.values() for a in b}


def one(lines):
    
    return sum(i for line in neartickets for i in line if i not in all_values)


def two(neartickets, yourticket):
    validtickets = [ticket for ticket in neartickets if all(i in all_values for i in ticket)]
    data_by_cols = list(zip(*validtickets))
    possible_cols = defaultdict(set)
    for name, nums in data.items():
        for idx, values in enumerate(data_by_cols):
            if all(v in nums for v in values):
                possible_cols[name].add(idx)

    print(possible_cols)

    
    print(sorted(possible_cols.items(), key=lambda i: i[1]))
    correct_cols = {}
    possible = set(possible_cols.keys())
    while possible:
        key, valueset = [(name, values) for name, values in possible_cols.items() if len(values) == 1][0]
        value = next(iter(valueset))
        print(f'got {value} for col {key}')
        correct_cols[key] = value
        for keys in possible_cols:
            try:
                possible_cols[keys].remove(value)
                if len(possible_cols[keys]) == 0:
                    possible.remove(keys)
            except KeyError:
                continue

    print(reduce(mul, (yourticket[i] for i in [6, 18, 19, 10, 7, 17])))

    print(correct_cols)


print(one(neartickets))
print(two(neartickets, yourticket))
