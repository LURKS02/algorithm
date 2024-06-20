from collections import deque

# N = 격자 한 변의 크기 (20)
# M = 색상의 개수 (5)
N, M = map(int, input().split())

board = []
totalBlocks = set()
INF = -float('inf')

for i in range(N):
    l = list(map(int, input().split()))
    for j in range(N):
        if l[j] == -1:
            totalBlocks.add((i, j))
    board.append(l)

def findBlockGroup(matrix):

    groupBlocks = set()
    groupRainbows = set()

    visited = [[False] * N for _ in range(N)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != -1 and matrix[i][j] != 0 and matrix[i][j] != INF:
                if not visited[i][j]:
                    blocks, rainbows = blockGroupInfo(matrix, i, j, visited)
                    lRainbows = list(rainbows)
                    for x, y in rainbows:
                        visited[x][y] = False

                    groupSize = len(groupBlocks) + len(groupRainbows)
                    testSize = len(blocks) + len(rainbows)
                    if groupSize < testSize:
                        groupBlocks = blocks
                        groupRainbows = rainbows

                    elif groupSize == testSize:
                        groupRainbowSize = len(groupRainbows)
                        testRainbowSize = len(rainbows)
                        if groupRainbowSize < testRainbowSize:
                            groupBlocks = blocks
                            groupRainbows = rainbows

                        elif groupRainbowSize == testRainbowSize:
                            groupBaseBlock = sorted(list(groupBlocks))[0]
                            testBaseBlock = sorted(list(blocks))[0]
                            if groupBaseBlock[0] < testBaseBlock[0]:
                                groupBlocks = blocks
                                groupRainbows = rainbows

                            elif groupBaseBlock[0] == testBaseBlock[0]:
                                if groupBaseBlock[1] < testBaseBlock[1]:
                                    groupBlocks = blocks
                                    groupRainbows = rainbows

    return (groupBlocks, groupRainbows)

def blockGroupInfo(matrix, x, y, visited):
    rainbows = set()
    colors = set()
    blockColor = matrix[x][y]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    deq = deque()
    deq.append((x, y))
    visited[x][y] = True
    colors.add((x, y))

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix) and not visited[nx][ny]:
                if matrix[nx][ny] == 0:
                    rainbows.add((nx, ny))
                    deq.append((nx, ny))
                    visited[nx][ny] = True
                elif matrix[nx][ny] == blockColor:
                    colors.add((nx, ny))
                    deq.append((nx, ny))
                    visited[nx][ny] = True

    return (colors, rainbows)

def plusScore(score, colors, rainbows):
    plusScore = pow(len(colors) + len(rainbows), 2)
    score += plusScore

    return score

def removeBlocks(matrix, colors, rainbows):
    lColors = list(colors)
    lRainbows = list(rainbows)

    for x, y in lColors:
        matrix[x][y] = INF
    for x, y in lRainbows:
        matrix[x][y] = INF

    return matrix

def gravity(board):
    for j in range(len(board)):
        stack = deque()
        emptyBlock = len(board)-1
        for i in range(len(board)-1, -2, -1):
            if board[i][j] == -1 or i == -1:
                while stack:
                    board[emptyBlock][j] = stack.popleft()
                    emptyBlock -= 1

                stack = deque()
                emptyBlock = i-1

            elif board[i][j] != INF:
                stack.append(board[i][j])
                board[i][j] = INF

    return board

def rotate(board):
    newBoard = [[float('inf')] * len(board) for _ in range(len(board))]

    for i in range(len(board)):
        l = board[i]

        for j in range(len(board)-1, -1, -1):
            newBoard[j][i] = l[len(board)-j-1]

    return newBoard

def testPrint(board):
    for i in range(N):
        print(*board[i])
    print()

score = 0
while True:
    colors, rainbows = findBlockGroup(board)
    if len(colors) + len(rainbows) < 2:
        print(score)
        break

    score = plusScore(score, colors, rainbows)
    board = removeBlocks(board, colors, rainbows)
    # testPrint(board)

    board = gravity(board)
    # testPrint(board)

    board = rotate(board)
    # testPrint(board)

    board = gravity(board)
    # testPrint(board)
