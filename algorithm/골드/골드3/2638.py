import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
cheese = [list(map(int, input().rstrip().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def airCheese(cheese):
    deq = deque([(0, 0)])
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[0][0] = True
    cheese[0][0] = 2

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and cheese[ny][nx] != 1:
                cheese[ny][nx] = 2
                visited[ny][nx] = True
                deq.append((nx, ny))

    return cheese

def meltCheese(x, y, cheese, melt, visited):
    deq = deque([(x, y)])

    visited[y][x] = True

    while deq:
        x, y = deq.popleft()

        airPoint = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and cheese[ny][nx] == 2:
                airPoint += 1
        if airPoint >= 2:
            melt.append((x, y))

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and cheese[ny][nx] == 1:
                visited[ny][nx] = True
                deq.append((nx, ny))

        # print(deq)

    return melt

time = 0

while True:
    melt = []
    cheese = airCheese(cheese)

    # for i in range(N):
    #     print(*cheese[i])
    # print()

    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 1:
                # print(i, j)
                meltCheese(j, i, cheese, melt, visited)

    # print(melt)

    for t in melt:
        cheese[t[1]][t[0]] = 2

    if len(melt) == 0:
        print(time)
        break

    time += 1
    # print(time)