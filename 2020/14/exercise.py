from itertools import product

with open('input.txt') as fp:
    lines = fp.read().splitlines()


def one(lines):
    mem = {}
    for line in lines:
        if line.startswith('mask'):
            mask = ['1' if c == '1' else '0' if c == '0' else None for c in line.lstrip('mask = ')]
        else:
            addr, val = line.split(' = ')
            addr = int(addr.strip('mem[]'))
            val = int(val)

            masked_val = [v if m is None else m for v, m in zip(format(val, '036b'), mask)]
            mem[addr] = int(''.join(masked_val), 2)

    return sum(mem.values())


def two(lines):
    mem = {}
    for line in lines:
        if line.startswith('mask'):
            mask = line.lstrip('mask = ')
        else:
            addr, val = line.split(' = ')
            addr = int(addr.strip('mem[]'))
            val = int(val)
            addr_bin = format(addr, '036b')
            masked_addr = ''.join(v if m == '0' else '1' if m == '1' else '{}' for v, m in zip(addr_bin, mask))
            for tup in product('01', repeat=masked_addr.count('{}')):
                new_addr = int(''.join(masked_addr).format(*tup), 2)
                mem[new_addr] = val

    return sum(mem.values())


print(one(lines))
print(two(lines))
