from collections import deque

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

remainedTomatoes = set()
goneTomatoes = []

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            remainedTomatoes.add((i, j))
        elif matrix[i][j] == 1:
            goneTomatoes.append((i, j))

deq = deque(goneTomatoes)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
days = 0

while deq:
    if len(remainedTomatoes) == 0:
        print(days)
        exit(0)

    temp = set()
    for tx, ty in deq:
        for i in range(4):
            nx, ny = tx + dx[i], ty + dy[i]

            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
                matrix[nx][ny] = 1
                temp.add((nx, ny))
                remainedTomatoes.remove((nx, ny))

    deq = deque(list(temp))
    days += 1

if len(remainedTomatoes) != 0:
    print(-1)
else:
    print(days)