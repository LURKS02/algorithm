from collections import deque
import bisect

N, S = map(int, input().split())

x = list(map(int, input().split()))
h = list(map(int, input().split()))

visited = set()
visited.add(S)

deq = deque()
deq.append(S)

while deq:
    idx = deq.popleft()

    ix = x[idx-1]
    ih = h[idx-1]

    maxRightPosition = ix + ih
    rightIdx = bisect.bisect_right(x, maxRightPosition)

    for i in range(idx+1, rightIdx+1):
        if i not in visited:
            visited.add(i)
            deq.append(i)

    maxLeftPosition = ix - ih
    leftIdx = bisect.bisect_left(x, maxLeftPosition)

    for i in range(leftIdx+1, idx):
        if i not in visited:
            visited.add(i)
            deq.append(i)

print(*sorted(visited))