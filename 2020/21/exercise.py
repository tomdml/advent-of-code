from collections import defaultdict, Counter
from functools import reduce

with open('input.txt') as fp:
    lines = fp.read().splitlines()

possible = defaultdict(list)
totals = Counter()
for line in lines:
    ingredients, allergens = line.split(' (contains ')
    ingredients = ingredients.split()
    allergens = allergens.rstrip(')').split(', ')

    totals.update(ingredients)

    for allergen in allergens:
        possible[allergen].append(set(ingredients))

actual = {
    allergen: reduce(set.intersection, sets)
    for allergen, sets in possible.items()
}

correct = {
    'fish': 'nhx',
    'soy': 'chbtp',
    'nuts': 'kfxr',
    'wheat': 'cqvc',
    'peanuts': 'xmhsbd',
    'sesame': 'rrjb',
    'shellfish': 'xzhxj',
    'eggs': 'ntft'
}

print(sum(count for key, count in totals.items() if key not in correct.values()))

print(','.join(correct[key] for key in sorted(correct.keys())))