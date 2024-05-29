from collections import deque
import sys

input = sys.stdin.readline
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
N, M = map(int, input().split())
s = [list(map(int, input().split())) for i in range(M)]
visited = [[False] * N for _ in range(M)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    room = 1

    while q:
        x, y = q.popleft()
        wall = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ((s[x][y] & wall) != wall):
                if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
                    room += 1
                    visited[nx][ny] = True
                    q.append((nx, ny))
            wall = wall * 2

    return room

roomCount = 0
maxRoom = 0
delRoom = 0

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            roomCount += 1
            maxRoom = max(maxRoom, bfs(i, j))

for i in range(M):
    for j in range(N):
        num = 1
        while num < 9:
            if num & s[i][j]:
                visited = [[False] * N for _ in range(M)]
                s[i][j] -= num
                delRoom = max(delRoom, bfs(i, j))
                s[i][j] += num
            num *= 2

print(roomCount)
print(maxRoom)
print(delRoom)