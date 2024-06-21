import sys
input = sys.stdin.readline

from collections import deque
from copy import deepcopy

R, C, T = map(int, input().rstrip().split())

A = [list(map(int, input().rstrip().split())) for _ in range(R)]
upperAirConditioner = (-1, -1)
lowerAirConditioner = (-1, -1)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(R):
    if A[i][0] == -1:
        upperAirConditioner = (i, 0)
        lowerAirConditioner = (i+1, 0)
        break

for _ in range(T):
    addedAirs = []
    tempMatrix = [[0] * C for _ in range(R)]
    tempMatrix[upperAirConditioner[0]][upperAirConditioner[1]] = -1
    tempMatrix[lowerAirConditioner[0]][lowerAirConditioner[1]] = -1

    for i in range(R):
        for j in range(C):
            if A[i][j] != -1 and A[i][j] != 0:
                spread = A[i][j] // 5
                cnt = 0
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < R and 0 <= nj < C and A[ni][nj] != -1:
                        addedAirs.append((ni, nj, spread))
                        cnt += 1
                remains = A[i][j] - spread * cnt
                tempMatrix[i][j] = remains

    for added in addedAirs:
        i, j, spread = added
        tempMatrix[i][j] += spread

    upperDeque = deque()
    for i in range(1, C):
        upperDeque.append(tempMatrix[upperAirConditioner[0]][i])
    for i in range(upperAirConditioner[0]-1, -1, -1):
        upperDeque.append(tempMatrix[i][C-1])
    for i in range(C-2, -1, -1):
        upperDeque.append(tempMatrix[0][i])
    for i in range(1, upperAirConditioner[0]):
        upperDeque.append(tempMatrix[i][0])
    tempMatrix[upperAirConditioner[0]][1] = 0
    for i in range(2, C):
        tempMatrix[upperAirConditioner[0]][i] = upperDeque.popleft()
    for i in range(upperAirConditioner[0]-1, -1, -1):
        tempMatrix[i][C-1] = upperDeque.popleft()
    for i in range(C-2, -1, -1):
        tempMatrix[0][i] = upperDeque.popleft()
    for i in range(1, upperAirConditioner[0]):
        tempMatrix[i][0] = upperDeque.popleft()
    upperDeque = deque()

    lowerDeque = deque()
    for i in range(1, C):
        lowerDeque.append(tempMatrix[lowerAirConditioner[0]][i])
    for i in range(lowerAirConditioner[0]+1, R):
        lowerDeque.append(tempMatrix[i][C-1])
    for i in range(C-2, -1, -1):
        lowerDeque.append(tempMatrix[R-1][i])
    for i in range(R-2, lowerAirConditioner[0], -1):
        lowerDeque.append(tempMatrix[i][0])

    tempMatrix[lowerAirConditioner[0]][1] = 0
    for i in range(2, C):
        tempMatrix[lowerAirConditioner[0]][i] = lowerDeque.popleft()
    for i in range(lowerAirConditioner[0]+1, R):
        tempMatrix[i][C-1] = lowerDeque.popleft()
    for i in range(C-2, -1, -1):
        tempMatrix[R-1][i] = lowerDeque.popleft()
    for i in range(R-2, lowerAirConditioner[0], -1):
        tempMatrix[i][0] = lowerDeque.popleft()
    lowerDeque = deque()

    A = deepcopy(tempMatrix)

s = 0
for i in range(R):
    s += sum(A[i])
print(s + 2)
