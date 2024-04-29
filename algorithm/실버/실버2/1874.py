import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
deq = deque()
count = 1
l = []
for _ in range(n):
    i = int(sys.stdin.readline().rstrip())
    if len(deq) == 0 or deq[-1] < i:
        for num in range(count, i + 1):
            deq.append(num)
            l.append('+')
            count += 1
        deq.pop()
        l.append('-')
    else:
        if deq.pop() != i:
            print('NO')
            l = []
            break
        else:
            l.append('-')
if l:
    for m in l:
        print(m)
