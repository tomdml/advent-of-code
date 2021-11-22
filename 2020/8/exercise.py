with open('input.txt') as fp:
    lines = fp.read().splitlines()
    inputs = [(line.split()[0], int(line.split()[1])) for line in lines]
"""
idx = 0
acc = 0
seen = set()
while idx not in seen:
    seen.add(idx)
    op, val = inputs[idx]
    if op == 'acc':
        acc += val
        idx += 1
    if op == 'jmp':
        idx += val
    if op == 'nop':
        idx += 1

print(acc)
"""
inputs_mod = []
for idx, line in enumerate(inputs):
    op, val = line
    if op == 'jmp':
        out = 'nop'
    elif op == 'nop':
        out = 'jmp'
    else:
        out = 'acc'
    inputs_mod.append([*inputs[:idx], (out, val), *inputs[idx + 1:]])

#print(inputs_mod)

for line in inputs_mod:
    idx = 0
    acc = 0
    seen = set()
    while idx not in seen:
        if idx >= len(inputs_mod):
            print(acc)
            break
        seen.add(idx)
        op, val = line[idx]
        if op == 'acc':
            acc += val
            idx += 1
        if op == 'jmp':
            idx += val
        if op == 'nop':
            idx += 1
    #print(idx)