import sys
from collections import deque
input = sys.stdin.readline

# N, M = 세로x가로 (1000x1000)
# K = 원하는 광물의 수 (1,000,000)
N, M, K = map(int, input().rstrip().split())

# S = 광물의 강도 (1 ~ 100,000)
S = []

possibleRocks = []

for i in range(N):
    l = list(map(int, input().rstrip().split()))
    if i == 0:
        for j in range(M):
            possibleRocks.append((i, j))
    else:
        possibleRocks.append((i, 0))
        possibleRocks.append((i, M-1))
    S.append(l)

start = 1
end = 1000000
ans = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while start <= end:
    mid = (start + end) // 2

    count = 0
    deq = deque()
    visited = [[False] * M for _ in range(N)]
    for x, y in possibleRocks:
        if S[x][y] <= mid:
            deq.append((x, y))
            visited[x][y] = True
            count += 1

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and S[nx][ny] <= mid:
                visited[nx][ny] = True
                count += 1
                deq.append((nx, ny))

    if count >= K:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)

