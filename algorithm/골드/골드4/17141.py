from collections import deque
from itertools import combinations
from copy import deepcopy

# N = 연구소의 크기 (50)
# M = 바이러스의 개수 (10)
N, M = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

board = []

canVirus = []
walls = []

for i in range(N):
    l = list(map(int, input().split()))
    board.append(l)
    for j in range(N):
        if l[j] == 2:
            canVirus.append((i, j))
        if l[j] == 1:
            walls.append((i, j))

def checkBoard(board):
    maxValue = -1
    for i in range(N):
        for j in range(N):
            if board[i][j] == -1:
                return -1
            maxValue = max(maxValue, board[i][j])

    return maxValue

minTime = float('inf')

for comb in combinations(canVirus, M):
    deq = deque()
    tempBoard = [[-1] * N for _ in range(N)]
    for vx, vy in walls:
        tempBoard[vx][vy] = -float('inf')

    for cx, cy in comb:
        deq.append((cx, cy))
        tempBoard[cx][cy] = 0

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if tempBoard[nx][ny] == -1:
                    deq.append((nx, ny))
                    tempBoard[nx][ny] = tempBoard[x][y] + 1

    # for i in range(N):
    #     print(*tempBoard[i])
    # print()

    check = checkBoard(tempBoard)
    if check != -1:
        minTime = min(minTime, check)



print(minTime) if minTime != float('inf') else print(-1)