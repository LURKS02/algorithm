import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

dict = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().rstrip().split())
    dict[B].append(A)
def bfs(n):
    deq = deque()
    visited = [0] * (N+1)
    visited[n] = 1
    count = 0

    deq.append(n)

    while(deq):
        num = deq.popleft()
        for i in dict[num]:
            if not visited[i]:
                visited[i] = 1
                deq.append(i)
                count += 1

    return count

ans = deque()
maxcom = 0

for i in range(1, N+1):
    num = bfs(i)
    if num > maxcom:
        maxcom = num
        ans.clear()
        ans.append(i)
    elif num == maxcom:
        ans.append(i)

print(*ans)