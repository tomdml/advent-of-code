from operator import add, mul


with open('input.txt') as fp:
    lines = fp.read().splitlines()


def parse(line):
    depth = 0
    for idx, char in enumerate(reversed(line)):
        if char == '(':
            depth += 1
        if char == ')':
            depth -= 1
        if char in '+*' and depth == 0:
            left = line[:-idx - 2]
            op = char
            right = line[-idx + 1:]
            return left, op, right
    # failed to split - must be a parenthesised expr.
    return parse(line[1:-1])


def parse2(line):
    depth = 0
    expr = ''
    for idx, char in enumerate(line.replace(' ', '')):

        expr += char

        if char == '(':
            depth += 1
        if char == ')':
            depth -= 1

        if char in '+*' and depth == 0:
            yield expr[:-1]
            yield char
            expr = ''

    if expr == line:
        yield from parse2(line[1:-1])
    else:
        yield expr

def calc(line):
    if line.isdigit():
        return int(line)
    head, oper, last = parse(line)
    ops = {'+': add, '*': mul}
    return ops[oper](calc(head), calc(last))


def first(lines):
    return sum(calc(line) for line in lines)


def calc2(line):
    if isinstance(line, int) or line.isdigit():
        return int(line)

    tokens = list(parse2(line))

    while '+' in tokens:
        idx = tokens.index('+')
        tokens[idx - 1: idx + 2] = [calc2(tokens[idx - 1]) + calc2(tokens[idx + 1])]

    while '*' in tokens:
        idx = tokens.index('*')
        tokens[idx - 1: idx + 2] = [calc2(tokens[idx - 1]) * calc2(tokens[idx + 1])]

    return tokens[0]


def second(lines):
    return sum(calc2(line) for line in lines)


print(first(lines))
print(second(lines))
