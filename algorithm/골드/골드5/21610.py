import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
matrix = []
moves = []

for _ in range(N):
    matrix.append(list(map(int, input().rstrip().split())))

for _ in range(M):
    d, s = map(int, input().rstrip().split())
    moves.append((d, s))

def moveClouds(clouds, d, s):
    movedClouds = []

    for cloud in clouds:
        cx, cy = cloud
        if d == 1:
            cx -= s
        elif d == 2:
            cx -= s
            cy -= s
        elif d == 3:
            cy -= s
        elif d == 4:
            cx += s
            cy -= s
        elif d == 5:
            cx += s
        elif d == 6:
            cx += s
            cy += s
        elif d == 7:
            cy += s
        elif d == 8:
            cx -= s
            cy += s

        # print("now: ", cx, cy)
        #
        # if cx < 0 or cx >= N:
        #     cx = (cx + N) % N + 1
        # if cy < 0 or cy >= N:
        #     cy = (cy + N) % N + 1

        if cx < 0:
            cx = (N + cx % N) % N

        elif cx >= N:
            cx = cx % N

        if cy < 0:
            cy = (N + cy % N) % N

        elif cy >= N:
            cy = cy % N

        # print("after: ", cx, cy)

        movedClouds.append((cx, cy))

    return movedClouds

def checkCopyWater(cloud):
    cx, cy = cloud

    dx = [-1, -1, 1, 1]
    dy = [1, -1, 1, -1]

    appendWater = 0

    for i in range(4):
        newX, newY = cx + dx[i], cy + dy[i]

        if 0 <= newX < N and 0 <= newY < N and matrix[newY][newX] > 0:
            appendWater += 1

    return appendWater

def createCloud(previousClouds):
    cloudSet = set(previousClouds)
    newClouds = []

    for i in range(N):
        for j in range(N):
            if matrix[i][j] >= 2 and (j, i) not in cloudSet:
                matrix[i][j] -= 2
                newClouds.append((j, i))

    return newClouds

def getSum():
    ans = 0

    for i in range(N):
        for j in range(N):
            ans += matrix[i][j]

    return ans

clouds = [(0, N-1), (1, N-1), (0, N-2), (1, N-2)]

for move in moves:
    d, s = move
    movedClouds = moveClouds(clouds, d, s)
    # print("movedClouds: ", movedClouds)

    for movedCloud in movedClouds:
        movedX, movedY = movedCloud
        matrix[movedY][movedX] += 1

    # for i in range(N):
    #     print(*matrix[i])

    for movedCloud in movedClouds:
        movedX, movedY = movedCloud
        matrix[movedY][movedX] += checkCopyWater(movedCloud)

    # for i in range(N):
    #     print(*matrix[i])


    clouds = createCloud(movedClouds)
    # for i in range(N):
    #     print(*matrix[i])

print(getSum())


