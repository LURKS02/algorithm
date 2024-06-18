from collections import deque
from itertools import permutations
from copy import deepcopy

N, M, K = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

# (가장 왼쪽 위 칸, 가장 오른쪽 아래 칸)
rotationList = []
for _ in range(K):
    r, c, s = map(int, input().split())
    rotationList.append(((r-s-1, c-s-1), (r+s-1, c+s-1)))

def getMinValue(matrix):
    minValue = float('inf')

    for i in range(len(matrix)):
        minValue = min(minValue, sum(matrix[i]))

    return minValue

def rotateMatrix(matrix, start, end):
    sx, sy = start
    ex, ey = end

    height = ex - sx + 1
    width = ey - sy + 1

    while height > 0 and width > 0:
        matrix = rotateSquare(matrix, (sx, sy), height, width)
        sx += 1
        sy += 1
        height -= 2
        width -= 2

    # for i in range(len(matrix)):
    #     print(*matrix[i])

    return matrix

def rotateSquare(matrix, start, height, width):
    if height == 1 and width == 1:
        return matrix

    if height == 1 and width == 2:
        matrix[0][0], matrix[0][1] = matrix[0][1], matrix[0][0]
        return matrix

    if height == 2 and width == 1:
        matrix[0][0], matrix[1][0] = matrix[1][0], matrix[0][0]
        return matrix

    deq = deque()
    x, y = start
    for i in range(width):
        deq.append(matrix[x][y+i])
    for i in range(1, height):
        deq.append(matrix[x+i][y+width-1])
    for i in range(width-2, -1, -1):
        deq.append(matrix[x+height-1][y+i])
    for i in range(height-2, 0, -1):
        deq.append(matrix[x+i][y])

    for i in range(1, width):
        matrix[x][y+i] = deq.popleft()
    for i in range(1, height):
        matrix[x+i][y+width-1] = deq.popleft()
    for i in range(width-2, -1, -1):
        matrix[x+height-1][y+i] = deq.popleft()
    for i in range(height-2, -1, -1):
        matrix[x+i][y] = deq.popleft()

    # for i in range(len(matrix)):
    #     print(*matrix[i])

    return matrix

minValue = float('inf')

for perm in permutations(rotationList, K):
    tempMatrix = deepcopy(A)

    for start, end in perm:
        tempMatrix = rotateMatrix(tempMatrix, start, end)

    minV = getMinValue(tempMatrix)
    minValue = min(minValue, minV)

print(minValue)