from collections import deque

def count(matrix):
    c = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                c += 1
    return c

def allMatrix(matrix):
    groups = []
    groups.append(matrix)
    tm = turnMatrix(matrix)
    groups.append(tm)
    tm2 = turnMatrix(tm)
    groups.append(tm2)
    tm3 = turnMatrix(tm2)
    groups.append(tm3)
    return groups

def turnMatrix(matrix):
    N = len(matrix)
    M = len(matrix[0])
    newMatrix = [[0] * N for _ in range(M)]

    for i in range(N-1, -1, -1):
        for j in range(M):
            newMatrix[j][N - i - 1] = matrix[i][j]
    return newMatrix

def makeMatrix(points):
    maxX, minX = -1, 51
    maxY, minY = -1, 51

    for px, py in points:
        maxX = max(maxX, px)
        minX = min(minX, px)
        maxY = max(maxY, py)
        minY = min(minY, py)

    xLength = maxX - minX + 1
    yLength = maxY - minY + 1

    tempMatrix = [[0] * yLength for _ in range(xLength)]

    for px, py in points:
        tempMatrix[px - minX][py - minY] = 1

    return tempMatrix

def dfs(x, y, matrix, base, visited):
    group = []
    N = len(matrix)
    deq = deque()
    deq.append((x, y))
    group.append((x, y))
    visited[x][y] = True
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while deq:
        cx, cy = deq.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == base and not visited[nx][ny]:
                group.append((nx, ny))
                visited[nx][ny] = True
                deq.append((nx, ny))
    return group

def solution(game_board, table):
    N = len(game_board)

    blankGroups = []
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and game_board[i][j] == 0:
                group = dfs(i, j, game_board, 0, visited)
                blankGroups.append(group)
    blankMatrices = []
    for group in blankGroups:
        m = makeMatrix(group)
        blankMatrices.append(m)

    puzzleGroups = []
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and table[i][j] == 1:
                group = dfs(i, j, table, 1, visited)
                puzzleGroups.append(group)
    puzzleMatrices = []
    for group in puzzleGroups:
        m = makeMatrix(group)
        puzzleMatrices.append(m)

    answer = 0
    used = [False] * len(puzzleMatrices)
    for matrix in blankMatrices:
        for i in range(len(puzzleMatrices)):
            if not used[i] and matrix in allMatrix(puzzleMatrices[i]):
                used[i] = True
                answer += count(matrix)
                break
    return answer

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))
print(solution([[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]]))