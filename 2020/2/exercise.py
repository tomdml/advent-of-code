import re

with open('input.txt') as fp:
    lines = []
    for line in fp:
        a, b, letter, password = re.split('[-: ]+', line)
        lines.append((int(a), int(b), letter, password))


def first(lines):
    return sum(
        a <= password.count(letter) <= b
        for a, b, letter, password
        in lines
    )


def second(lines):
    return sum(
        (password[a - 1] == letter) ^ (password[b - 1] == letter)
        for a, b, letter, password
        in lines
    )


print(first(lines))
print(second(lines))
