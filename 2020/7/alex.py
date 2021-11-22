import re


def checkbag(set, bagdict, soughtbag, givenbag):
    if soughtbag in bagdict[givenbag]:
        print(givenbag + ' ' + str(bagdict[givenbag]))
        set.add(givenbag)
        return True

    for b in bagdict[givenbag]:
        if b != 'noother' and checkbag(set, bagdict, soughtbag, b):
            set.add(givenbag)
            print(givenbag + ' ' + str(bagdict[givenbag]))


with open(r'input.txt') as fp:
    text = fp.read()
    text = re.sub(r' bags| bag|\.| \d | ', '', text)
    text = text.replace('contain', ':')
    text = [line.split(':') for line in text.splitlines()]

    bags = {entry[0]: entry[1].split(',') for entry in text}

#    print(bags)

    validbags = set()

    for key in bags.keys():
        checkbag(validbags, bags, 'shinygold', key)
    print(bags)
    print(validbags)
    print(len(validbags))
