with open('input.txt') as fp:
    lines = [(line[0], int(line[1:])) for line in fp.read().splitlines()]

def one(lines):
    direction = 0 # east
    ns = 0
    ew = 0

    for op, num in lines:
        if op == 'N':
            ns += num
        if op == 'S':
            ns -= num
        if op == 'E':
            ew += num
        if op == 'W':
            ew -= num
        if op == 'F':
            if direction == 0:
                ew += num
            if direction == 180:
                ew -= num
            if direction == 90:
                ns -= num
            if direction == 270:
                ns += num
        if op == 'L':
            direction -= num
        if op == 'R':
            direction += num
        if direction >= 360:
            direction %= 360
        if direction < 0:
            direction = direction + 360

    return abs(ew) + abs(ns)

def two(lines):
    offset_ns = 1
    offset_ew = 10
    ns = 0
    ew = 0

    for op, num in lines:
        if op == 'N':
            offset_ns += num
        if op == 'S':
            offset_ns -= num
        if op == 'E':
            offset_ew += num
        if op == 'W':
            offset_ew -= num

        if op == 'F':
            ns += (num * offset_ns)
            ew += (num * offset_ew)

        if op == 'L':
            direction = num
        elif op == 'R':
            direction = (360 - num)
        else:
            direction = 0

        if direction == 90:
            offset_ew, offset_ns = -offset_ns, offset_ew

        if direction == 180:
            offset_ew, offset_ns = -offset_ew, -offset_ns

        if direction == 270:
            offset_ew, offset_ns = offset_ns, -offset_ew

    return abs(ew) + abs(ns)

print(one(lines))
print(two(lines))