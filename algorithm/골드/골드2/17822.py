from collections import deque

N, M, T = map(int, input().split())
numbers = [deque()]

for _ in range(N):
    l = list(map(int, input().split()))
    numbers.append(deque(l))

def bfs(x, y):
    global bfsed
    deq = deque([(x, y)])
    value = numbers[x][y]
    groups = [(x, y)]

    visited = [[False] * M for _ in range(N+1)]
    visited[x][y] = True

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while deq:
        curX, curY = deq.popleft()

        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]

            if ny == -1:
                ny = M-1
            if ny == M:
                ny = 0

            if 1 <= nx < N+1 and 0 <= ny < M and not visited[nx][ny] and numbers[nx][ny] == value:
                groups.append((nx, ny))
                deq.append((nx, ny))
                visited[nx][ny] = True

    # print(groups)
    if len(groups) > 1:
        for gx, gy in groups:
            numbers[gx][gy] = 0
        bfsed = True


for _ in range(T):
    x, d, k = map(int, input().split())

    for i in range(x, N+1, x):
        if d == 0:
            numbers[i].rotate(k)
        else:
            numbers[i].rotate(-k)

    # for i in range(1, N + 1):
    #     print(*numbers[i])
    # print()

    bfsed = False

    for i in range(N+1):
        if i == 0: continue
        for j in range(M):
            if numbers[i][j] != 0:
                bfs(i, j)

    if not bfsed:
        totalSum = 0
        totalNum = 0

        for i in range(1, N+1):
            for j in range(M):
                if numbers[i][j] != 0:
                    totalSum += numbers[i][j]
                    totalNum += 1

        if totalNum != 0:
            avg = totalSum / totalNum
            # print(avg)

            for i in range(1, N+1):
                for j in range(M):
                    if numbers[i][j] != 0:
                        if numbers[i][j] < avg:
                            numbers[i][j] += 1
                        elif numbers[i][j] > avg:
                            numbers[i][j] -= 1

    # for i in range(1, N+1):
    #     print(*numbers[i])
    # print()

s = 0
for i in range(1, N+1):
    for j in range(M):
        s += numbers[i][j]

print(s)