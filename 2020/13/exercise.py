from sympy.ntheory.modular import crt

with open('input.txt') as fp:
    timestamp, buses = fp.readlines()
    timestamp = int(timestamp)
    buses = [(idx, int(bus)) for idx, bus in enumerate(buses.split(',')) if bus != 'x']


def one(timestamp, buses):
    start = timestamp
    while True:
        for bus in buses:
            if not timestamp % bus:
                return (timestamp-start)*bus
        timestamp += 1


def two(lines):
    M = [mod for idx, mod in buses]
    U = [idx for idx, mod in buses]
    return crt(M, U)


# print(one(timestamp, buses))
print(two(buses))