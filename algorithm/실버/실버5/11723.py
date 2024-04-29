import sys

M = int(input())

S = set()

def add(x):
    global S
    S.add(x)

def remove(x):
    global S
    S.discard(x)

def check(x):
    global S
    if x in S:
        print('1')
    else:
        print('0')

def toggle(x):
    global S
    if x in S:
        S.remove(x)
    else:
        S.add(x)

def all():
    global S
    S = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

def empty():
    global S
    S.clear()

for i in range(M):
    insert = list(sys.stdin.readline().rstrip().split())

    if len(insert) == 1:
        if insert[0] == 'all':
            all()
        elif insert[0] == 'empty':
            empty()

    else:
        inst = insert[0]
        num = int(insert[1])

        if inst == 'add':
            add(num)
        elif inst == 'remove':
            remove(num)
        elif inst == 'check':
            check(num)
        elif inst == 'toggle':
            toggle(num)