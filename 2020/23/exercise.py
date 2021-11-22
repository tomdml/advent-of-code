from collections import deque

cups = deque('389125467')
current = '3'
cups.rotate(-cups.index(current))
cups.rotate(-1)



def step(cups, current):


for _ in range(100):
    cups, current = step(cups, current)

print(cups)