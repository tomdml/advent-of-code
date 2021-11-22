from collections import defaultdict
from functools import lru_cache

with open('input.txt') as fp:
    lines = fp.read().splitlines()

bags = defaultdict(list)
for line in lines:
    colour, contents = line.strip('.').split(' bags contain ')
    if contents == 'no other bags':
        bags[colour] = []
    else:
        for item in contents.split(', '):
            qty, desc1, desc2, _ = item.split()
            bags[colour] += (int(qty), f"{desc1} {desc2}"),


def find(colour):
    if any(colour in (col for qty, col in bags[colour]))
    if colour in (col for qty, col in bags[target]):
        return True
    return sum(
        find(colour)
        for colour
        in bags
    )


@lru_cache()
def count(colour):
    return sum(
        qty * (1 + count(bag))
        for qty, bag
        in bags[colour]
    )

print(bags)
print(find('shiny gold'))
print(count('shiny gold'))
