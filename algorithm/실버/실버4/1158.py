from collections import deque

N, K = map(int, input().split())

deq = deque(range(1, N + 1))

print('<', end='')
while(deq):
    deq.rotate(-K + 1)
    print(deq.popleft(), end='')
    if len(deq) is not 0:
        print(', ', end='')

print('>', end='')


