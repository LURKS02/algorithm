from collections import deque

N, M = map(int, input().split())

matrix = [list(input()) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    visited = [[False for _ in range(M)] for _ in range(N)]
    deq = deque()
    deq.append((x, y, 0))
    visited[y][x] = True

    maxWay = -1

    while(deq):
        currentX, currentY, count = deq.popleft()
        maxWay = max(maxWay, count)

        for i in range(4):
            newX, newY = currentX + dx[i], currentY + dy[i]
            # print(newX, newY)
            if 0 <= newX < M and 0 <= newY < N and not visited[newY][newX] and matrix[newY][newX] == 'L':
                deq.append((newX, newY, count + 1))
                visited[newY][newX] = True

    return maxWay

maxCount = -1

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'L':
            maxCount = max(maxCount, bfs(j, i))

print(maxCount)