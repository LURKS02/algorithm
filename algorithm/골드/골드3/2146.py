from collections import deque

N = int(input())

map = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(matrix, x, y, visited, mark):
    deq = deque([(x, y)])
    visited[y][x] = True

    matrix[y][x] = mark

    while deq:
        currentX, currentY = deq.popleft()

        for i in range(4):
            newX, newY = currentX + dx[i], currentY + dy[i]
            if 0 <= newX < N and 0 <= newY < N and matrix[newY][newX] == 1 and not visited[newY][newX]:
                visited[newY][newX] = True
                matrix[newY][newX] = mark
                deq.append((newX, newY))

visited = [[False for _ in range(N)] for _ in range(N)]

def distance(matrix, x, y):
    visited = [[False for _ in range(N)] for _ in range(N)]
    deq = deque([(x, y, 0)])
    mark = matrix[y][x]

    while deq:
        currentX, currentY, count = deq.popleft()

        if matrix[currentY][currentX] != 0 and matrix[currentY][currentX] != mark:
            return count

        for i in range(4):
            newX, newY = currentX + dx[i], currentY + dy[i]
            if 0 <= newX < N and 0 <= newY < N and not visited[newY][newX]:
                visited[newY][newX] = True
                deq.append((newX, newY, count + 1))

mark = 2
for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and not visited[i][j]:
            bfs(map, j, i, visited, mark)
            mark += 1

# for i in range(N):
#     print(*map[i])

minValue = float('inf')

for i in range(N):
    for j in range(N):
        c = 0
        for k in range(4):
            ni, nj = i + dy[k], j + dx[k]
            if 0 <= ni < N and 0 <= nj < N and map[ni][nj] == 0:
                c += 1

        if c > 0 and map[i][j] != 0:
            d = distance(map, j, i)
            if minValue > d:
                minValue = d

print(minValue - 1)

