with open('input.txt') as fp:
    passes = fp.read().splitlines()


def getid(line):
    td = str.maketrans('FLBR', '0011')
    return int(line.translate(td), 2)


ids = {getid(line) for line in passes}
missing = set(range(len(ids))) - set(ids)

print('Part 1:', max(ids))

for item in missing:
    if item - 1 in ids and item + 1 in ids:
        print('Part 2:', item)
