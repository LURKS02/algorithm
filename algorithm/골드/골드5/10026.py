from collections import deque

N = int(input())

matrix = []
converted_matrix = []

for _ in range(N):
    matrix.append([c for c in input()])

# print(matrix)

for i in range(N):
    newLine = []
    for c in matrix[i]:
        if c == 'G':
            newLine.append('R')
        else:
            newLine.append(c)
    converted_matrix.append(newLine)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(matrix, x, y, N, visited):
    deq = deque()
    deq.append((x, y))
    pivot = matrix[y][x]
    # print("pivot = ", pivot)
    visited[y][x] = True

    while(deq):
        # print(deq)
        currentX, currentY = deq.pop()

        for i in range(4):
            newX, newY = currentX + dx[i], currentY + dy[i]
            # print(newX, newY)
            # if 0 <= newX < N and 0 <= newY < N:
            #     print(visited[newY][newX], matrix[newY][newX])

            if 0 <= newX < N and 0 <= newY < N and not visited[newY][newX] and matrix[newY][newX] == pivot:
                visited[newY][newX] = True
                deq.append((newX, newY))

    return 1

visited = [[False for _ in range(N)] for _ in range(N)]
totalNon = 0
total = 0
for i in range(N):
    for j in range(N):
        if not visited[j][i]:
            totalNon += dfs(matrix, i, j, N, visited)
            # for k in range(N):
            #     print(*visited[k])
            # print()

visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[j][i]:
            total += dfs(converted_matrix, i, j, N, visited)

print(totalNon, total)