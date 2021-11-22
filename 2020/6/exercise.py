with open('input.txt') as fp:
    lines = [group.splitlines() for group in fp.read().split('\n\n')]
    sets = [[set(answer) for answer in group] for group in lines]

q1 = sum(
    len(set.union(*group))
    for group
    in sets
)

q2 = sum(
    len(set.intersection(*group))
    for group
    in sets
)

print(q1)
print(q2)
