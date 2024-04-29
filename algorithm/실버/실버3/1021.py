from collections import deque

N, M = map(int, input().split())
l = list(map(int, input().split()))

deq = deque(range(1, N + 1))

count = 0
for num in l:
    if deq[0] == num:
        deq.popleft()
    else:
        index = -1
        for i in range(len(deq)):
            if deq[i] == num:
                index = i
                break
        if index <= len(deq) - index:
            deq.rotate(-index)
            count += index
            deq.popleft()
        else:
            deq.rotate(len(deq) - index)
            count += len(deq) - index
            deq.popleft()

print(count)