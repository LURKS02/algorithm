import sys
from collections import deque

N = int(input())
q = deque()

for _ in range(N):
    inputString = sys.stdin.readline().strip().split()
    if len(inputString) == 1:
        if inputString[0] == 'pop_front':
            if len(q) == 0:
                print(-1)
            else:
                print(q.popleft())
        elif inputString[0] == 'pop_back':
            if len(q) == 0:
                print(-1)
            else:
                print(q.pop())
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
        operator = inputString[0]
        X = int(inputString[1])
        if operator == 'push_front':
            q.appendleft(X)
        elif operator == 'push_back':
            q.append(X)
