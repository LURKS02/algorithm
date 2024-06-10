from collections import deque

N = int(input())
K = int(input())

apples = []

for _ in range(K):
    row, col = map(int, input().split())
    apples.append((row-1, col-1))

L = int(input())
times = set()
directions = []
for _ in range(L):
    time, dir = input().split()
    times.add(int(time))
    directions.append(dir)

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
curDir = 0

time = 0
dirIdx = 0

snakeSet = set()
snakeSet.add((0, 0))
snakes = deque()
snakes.append((0, 0))

while True:
    if time in times:
        dir = directions[dirIdx]
        if dir == 'L':
            curDir = (curDir - 1 + 4) % 4
        else:
            curDir = (curDir + 1) % 4
        dirIdx += 1

    headX, headY = snakes[-1]
    newX, newY = headX + dx[curDir], headY + dy[curDir]

    if newX < 0 or newX >= N or newY < 0 or newY >= N or (newX, newY) in snakeSet:
        print(time + 1)
        exit(0)

    if (newX, newY) in apples:
        apples.remove((newX, newY))
        snakes.append((newX, newY))
        snakeSet.add((newX, newY))

    else:
        snakes.append((newX, newY))
        popX, popY = snakes.popleft()
        snakeSet.add((newX, newY))
        snakeSet.remove((popX, popY))

    time += 1


