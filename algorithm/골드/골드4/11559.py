from collections import deque

matrix = []

for i in range(12):
    matrix.append([s for s in input()])

# print(matrix)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(matrix, x, y, visited):
    deq = deque([(x, y)])
    visited[y][x] = True
    pivot = matrix[y][x]

    removed = [(x, y)]

    while deq:
        currentX, currentY = deq.popleft()

        for i in range(4):
            newX, newY = currentX + dx[i], currentY + dy[i]

            if 0 <= newX < 6 and 0 <= newY < 12 and not visited[newY][newX] and matrix[newY][newX] == pivot:
                visited[newY][newX] = True
                removed.append((newX, newY))
                deq.append((newX, newY))

    if len(removed) >= 4:
        for rx, ry in removed:
            matrix[ry][rx] = '.'
        return True

    return False

def sortMatrix(matrix):
    for j in range(6):
        blank = 12
        for i in range(11, -1, -1):
            if matrix[i][j] != '.':
                if blank != 12:
                    matrix[blank][j] = matrix[i][j]
                    matrix[i][j] = '.'

                    while blank >= 0:
                        blank -= 1
                        if matrix[blank][j] == '.':
                            break

            else:
                if blank == 12:
                    blank = i

popCount = 0
while True:
    visited = [[False for _ in range(6)] for _ in range(12)]

    matrixChanged = False

    for i in range(12):
        for j in range(6):
            if matrix[i][j] != '.' and not visited[i][j]:
                if bfs(matrix, j, i, visited):
                    matrixChanged = True

    if not matrixChanged:
        print(popCount)
        break

    popCount += 1

    # for i in range(12):
    #     print(*matrix[i])
    #
    # print()

    sortMatrix(matrix)

    # for i in range(12):
    #     print(*matrix[i])
    #
    # print()