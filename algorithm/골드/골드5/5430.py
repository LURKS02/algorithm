import sys
from collections import deque

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    p = input().rstrip()
    n = int(input().rstrip())

    inp = input().rstrip()
    nums = list(map(int, inp[1:-1].split(','))) if inp != '[]' else []

    if len(nums) < p.count('D'):
        print('error')

    else:
        deq = deque(nums)

        removeLeft = True
        Rcount = 0
        i = 0
        while i < len(p):
            if p[i] == 'R':
                removeLeft = removeLeft ^ True
                Rcount += 1

            if p[i] == 'D':
                if removeLeft:
                    deq.popleft()
                else:
                    deq.pop()
            i += 1
        print('[', end='')
        if Rcount % 2 == 0:
            l = list(deq)
            for i in range(len(l)):
                print(l[i], end='')
                if i != len(l)-1:
                    print(',', end='')
        else:
            l = list(deq)
            for i in range(len(l)-1, -1, -1):
                print(l[i], end='')
                if i != 0:
                    print(',', end='')
        print(']', end='')
        print()