from itertools import product

with open('input.txt') as fp:
    lines = fp.read().splitlines()
    alive = {(r, c, 0, 0) for r, row in enumerate(lines) for c, cell in enumerate(row) if cell == '#'}


def nbors(cell, dimensions):
    return (
        (orig + diff for orig, diff in zip(cell, differences))
        for differences
        in product((-1, 0, 1), repeat=dimensions)
    )


def nearest(alive, cell, dimensions):
    return sum(coords in alive for coords in nbors(cell, dimensions)) - (cell in alive)


def solution(alive, dimensions, steps):

    def step(alive):
        new_alive = set()
        candidates = {nbor for cell in alive for nbor in nbors(cell, dimensions)}
        for cell in candidates:
            near = nearest(alive, cell, dimensions)
            if cell in alive and near in (2, 3) or cell not in alive and near == 3:
                new_alive.add(cell)

        return new_alive

    for _ in range(steps):
        alive = step(alive)

    return len(alive)


print(solution(alive, 3, 6))
print(solution(alive, 4, 6))
