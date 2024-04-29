import sys
from collections import deque

q = deque()

N = int(input())

for _ in range(N):
    inputString = sys.stdin.readline().strip().split()
    if len(inputString) == 1:
        if inputString[0] == 'pop':
            if len(q) == 0:
                print(-1)
            else:
                print(q.popleft())
        elif inputString[0] == 'size':
            print(len(q))
        elif inputString[0] == 'empty':
            if len(q) == 0:
                print(1)
            else:
                print(0)
        elif inputString[0] == 'front':
            if len(q) == 0:
                print(-1)
            else:
                print(q[0])
        elif inputString[0] == 'back':
            if len(q) == 0:
                print(-1)
            else:
                print(q[-1])
    else:
        num = inputString[1]
        q.append(num)


