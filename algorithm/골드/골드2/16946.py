from collections import deque

N, M = map(int, input().split())
matrix = [[int(c) for c in input()] for _ in range(N)]
zeroMatrix = [[0] * M for _ in range(N)]
groupCount = {}

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, matrix, group):
    count = 1

    deq = deque()
    deq.append((x, y))
    matrix[x][y] = group

    while deq:
        curX, curY = deq.popleft()

        for i in range(4):
            newX, newY = curX + dx[i], curY + dy[i]
            if 0 <= newX < N and 0 <= newY < M and matrix[newX][newY] == 0:
                count += 1
                matrix[newX][newY] = group
                deq.append((newX, newY))

    return count

groupNumber = 2
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            groupCount[groupNumber] = bfs(i, j, matrix, groupNumber)
            groupNumber += 1

# for i in range(N):
#     for j in range(M):
#         print(matrix[i][j], end='')
#     print()

# print(groupCount)

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            check = set()
            cnt = 0
            for k in range(4):
                newI, newJ = i + dx[k], j + dy[k]
                if 0 <= newI < N and 0 <= newJ < M and matrix[newI][newJ] != 1 and matrix[newI][newJ] not in check:
                    cnt += groupCount[matrix[newI][newJ]]
                    check.add(matrix[newI][newJ])
            zeroMatrix[i][j] = (cnt + 1) % 10

for i in range(N):
    for j in range(M):
        print(zeroMatrix[i][j], end='')
    print()