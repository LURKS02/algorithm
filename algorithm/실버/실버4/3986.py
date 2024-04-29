from collections import deque

N = int(input())

count = 0

def verify(deq, str):
    for c in str:
        if len(deq) > 0 and c == deq[-1]:
            deq.pop()
        else:
            deq.append(c)
    if len(deq) == 0:
        return 1
    else:
        return 0

for _ in range(N):
    inputString = input()

    deq = deque()
    count += verify(deq, inputString)

print(count)

