with open('input.txt') as fp:
    players = fp.read().split('\n\n')
    orig_p1, orig_p2 = [[int(n) for n in player.splitlines()[1:]][::-1] for player in players]
    p1, p2 = orig_p1.copy(), orig_p2.copy()


def round(p1, p2):
    p1card, p2card = p1.pop(), p2.pop()

    if p1card > p2card:
        p1 = [min((p1card, p2card)), max((p1card, p2card))] + p1
    else:
        p2 = [min((p1card, p2card)), max((p1card, p2card))] + p2

    return p1, p2


def rec_round(p1, p2):
    #print('\ndecks are', p1, p2)
    p1card, p2card = p1.pop(), p2.pop()
    #print('p1 plays', p1card, 'p2 plays', p2card)

    if len(p1) >= p1card and len(p2) >= p2card:
        t1, t2 = rec_game(p1[-p1card:], p2[-p2card:])
        if t1:
            p1 = [p2card, p1card] + p1
        else:
            p2 = [p1card, p2card] + p2
    else:
        if p1card > p2card:
            p1 = [min((p1card, p2card)), max((p1card, p2card))] + p1
        else:
            p2 = [min((p1card, p2card)), max((p1card, p2card))] + p2

    return p1, p2

# part 1
while p1 and p2:
    p1, p2 = round(p1, p2)

winner = p1 or p2
print('part 1', sum(card * score for card, score in zip(winner[::-1], range(len(winner), 0, -1))))


# part 2
def rec_game(p1, p2):
    #print('playing game with', p1, p2)
    seen = set()
    while p1 and p2:

        if frozenset(p1) in seen:
            return p1, []
        seen.add(frozenset(p1))

        p1, p2 = rec_round(p1, p2)

    return p1, p2


p1, p2 = rec_game(orig_p1, orig_p2)
print(p1, p2)

winner = p1 or p2
print('part 2', sum(card * score for card, score in zip(winner[::-1], range(len(winner), 0, -1))))
