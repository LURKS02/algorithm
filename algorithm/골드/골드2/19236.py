from copy import deepcopy

matrix = [[] for _ in range(4)]
matrix[0].append([0, -1])

sx = 0
sy = 0
totalCount = 0
direction = -1

for i in range(4):
    l = list(map(int, input().split()))
    for j in range(4):
        if i == 0 and j == 0:
            totalCount = l[0]
            direction = l[1]
        else:
            matrix[i].append([l[j*2], l[j*2+1]])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def shark(matrix, sx, sy, count, direction):
    # print(count)
    global totalCount

    # 1부터 16까지 체크
    for k in range(1, 17):

        changed = False
        for i in range(4):
            for j in range(4):
                if matrix[i][j][0] != k or changed:
                    continue

                dir = matrix[i][j][1]
                for _ in range(8):
                    nx, ny = i + dx[dir-1], j + dy[dir-1]
                    if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == sx and ny == sy):
                        tempFish = matrix[nx][ny][0]
                        tempDir = matrix[nx][ny][1]
                        matrix[nx][ny][0] = k
                        matrix[nx][ny][1] = dir
                        matrix[i][j][0] = tempFish
                        matrix[i][j][1] = tempDir
                        changed = True
                        break
                    dir = (dir + 1)%9

        # for i in range(4):
        #     print(matrix[i])
        # print()

    nsx, nsy = sx, sy
    heap = []
    nsx += dx[direction-1]
    nsy += dy[direction-1]
    while 0 <= nsx < 4 and 0 <= nsy < 4:
        if matrix[nsx][nsy][0] != 0:
            heap.append((nsx, nsy))

        nsx += dx[direction-1]
        nsy += dy[direction-1]

    if len(heap) == 0:
        totalCount = max(totalCount, count)

    else:
        for x, y in heap:
            tempMatrix = deepcopy(matrix)
            tempMatrix[x][y][0] = 0
            tempMatrix[x][y][1] = -1
            shark(tempMatrix, x, y, count + matrix[x][y][0], matrix[x][y][1])


shark(matrix, sx, sy, totalCount, direction)

print(totalCount)