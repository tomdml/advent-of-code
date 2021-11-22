from functools import reduce
from operator import mul

with open('input.txt') as fp:
    forest = fp.readlines()

    repeat_x = len(forest[0])
    target_y = len(forest)

    trees = {
        (x, y)
        for y, row in enumerate(forest)
        for x, cell in enumerate(row)
        if cell == '#'
    }


def num_trees(trees, dx, dy):
    coords = {
        (x % (repeat_x - 1), y)
        for x, y in zip(
            range(0, target_y * dx, dx),
            range(0, target_y, dy))
    }
    return len(coords & trees)


steps = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
one = num_trees(trees, 3, 1)
two = reduce(mul, (num_trees(trees, dx, dy) for dx, dy in steps))
print(one, two)
