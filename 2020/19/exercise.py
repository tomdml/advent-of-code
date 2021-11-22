"""
with open('data.txt') as fp:
    data = fp.read().splitlines()


with open('rules.txt') as fp:
    lines = fp.read().splitlines()

    rules = {}
    for line in lines:
        idx, rule = line.split(': ')
        idx = int(idx)
        if rule in ('"a"', '"b"'):
            rules[idx] = rule.strip('"')
        else:
            options = rule.split(' | ')
            options = [[int(n) for n in option.split(' ')] for option in options]
            rules[idx] = options

    print(rules)


def test(rule, substr):
    return 0


print(sum(test(0, line) for line in data))
"""

# MUST REDO THIS ONE IN OWN TIME!!!
import re

rules, strings = [l.rstrip('\n') for l in open('input.txt').read().split('\n\n')]

rules = dict([rule.split(': ', 1) for rule in rules.split('\n')])
def getre(rulenum):
    # for part 1, delete these two rules:
    
    if rulenum == '8':
        return getre('42') + '+'
    elif rulenum == '11':
        a = getre('42')
        b = getre('31')
        return '(?:' + '|'.join(f'{a}{{{n}}}{b}{{{n}}}' for n in range(1, 100)) + ')'
    
    rule = rules[rulenum]
    if re.fullmatch(r'"."', rule):
        return rule[1]
    else:
        parts = rule.split(' | ')
        res = []
        for part in parts:
            nums = part.split(' ')
            res.append(''.join(getre(num) for num in nums))
        return '(?:' + '|'.join(res) + ')'


z = getre('0')
ct = 0
for string in strings.split('\n'):
    ct += bool(re.fullmatch(z, string))
print(ct)