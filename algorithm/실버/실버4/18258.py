from collections import deque
import sys

deq = deque()

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    query = sys.stdin.readline().rstrip().split()
    if len(query) == 1:
        if query[0] == 'size':
            print(len(deq))
        elif query[0] == 'pop':
            if len(deq) == 0:
                print(-1)
            else:
                print(deq.popleft())
        elif query[0] == 'empty':
            if len(deq) == 0:
                print(1)
            else:
                print(0)
        elif query[0] == 'front':
            if len(deq) == 0:
                print(-1)
            else:
                print(deq[0])
        elif query[0] == 'back':
            if len(deq) == 0:
                print(-1)
            else:
                print(deq[-1])
    else:
        deq.append(query[1])


