with open('input.txt') as fp:
    lines = fp.read().splitlines()
    max_row = len(lines)
    max_col = len(lines[0])
    empty = {(r, c) for r, row in enumerate(lines) for c, cell in enumerate(row) if cell == 'L'}


def nearest_8(chairs, r, c):
    return sum(
        (new_r, new_c) in chairs
        for new_r, new_c
        in [
            (r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
            (r,     c - 1),             (r,     c + 1), # noqa
            (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)
        ]
    )


def visible_8(chairs, r, c):

    def first(r, c, dr, dc):
        while 0 <= r < max_row and 0 <= c < max_col:
            r += dr
            c += dc
            if (r, c) in empty:
                return ('L', (r, c))
            if (r, c) in occupied:
                return ('#', (r, c))

    def visible(r, c):
        steps = ((-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, 0-1), (+1, 0), (+1, +1))
        result = []
        for dr, dc in steps:
            nextseat = first(r, c, dr, dc)
            if nextseat:
                result.append(nextseat)
        return result


def solution(current_empty, nbor_func, nbor_count):

    def step(empty, occupied):
        new_occupied, new_empty = set(), set()

        for r, c in occupied:
            visible_occupied = nbor_func(occupied, r, c)
            (new_occupied if visible_occupied >= nbor_count else new_empty).add((r, c))

        for r, c in empty:
            visible_empty = nbor_func(empty, r, c)
            (new_occupied if visible_empty == 0 else new_empty).add((r, c))

        return new_empty, new_occupied

    count = 0
    current_occupied = set()
    while new_board := step(current_empty, current_occupied) != (current_empty, current_occupied):
        new_empty, new_occupied = new_board
        count += 1

    return len(new_occupied)


print(solution(empty, nearest_8, 4))
print(solution(empty, visible_8, 5))
