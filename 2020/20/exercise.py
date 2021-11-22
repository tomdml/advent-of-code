from functools import reduce
from operator import mul


class Tile:
    def __init__(self, lines):
        self.text = lines

    def rotate(self):
        # A 90 degree clockwise rotation is the same as transposing then reversing each row.
        self.text = [row[::-1] for row in zip(*self.text)]

    def flip(self):
        self.text = [row[::-1] for row in self.text]

    def touching(self, other):
        if self is other:
            return False

        other_edges = {other.top, other.top[::-1], other.bottom, other.bottom[::-1], other.left, other.left[::-1], other.right, other.right[::-1]}
        return {self.top, self.bottom, self.left, self.right} & other_edges

    @property
    def top(self):
        return self.text[0]

    @property
    def bottom(self):
        return self.text[-1]

    @property
    def left(self):
        return ''.join(line[0] for line in self.text)

    @property
    def right(self):
        return ''.join(line[-1] for line in self.text)

    @property
    def inner(self):
        return [line[1:-1] for line in self.text[1:-1]]


with open('input.txt') as fp:
    tiles = [tile.splitlines() for tile in fp.read().split('\n\n')]

tiledict = {int(name.strip('Tile :')): Tile(lines) for name, *lines in tiles}

neighbours = {
    name: [
        other_name
        for other_name, other_tile
        in tiledict.items()
        if tile.touching(other_tile)
    ]
    for name, tile
    in tiledict.items()}


def one(tiledict):
    return reduce(mul, [name for name, nbors in neighbours.items() if len(nbors) == 2])


def two(tiledict, neighbours):
    # get a 2-connection vertex
    twos = [name for name, nbors in neighbours.items() if len(nbors) == 2]
    current_node = twos[0]
    

    return to_visit


print(one(tiledict))
#print(two(tiledict, neighbours))
