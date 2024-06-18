from collections import deque

# N = 격자의 크기 (20)
# M = 상어의 수 (400)
# K = 냄새가 사라지는 이동 횟수 (1000)
N, M, K = map(int, input().split())

# 위, 아래, 왼쪽, 오른쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# [[2, 0, 3], [1, 1, 3], [0, 4, 2], [2, 4, 0]] 초기 상어의 x, y, 방향
sharks = [[-1, -1]] * M

for i in range(N):
    l = list(map(int, input().split()))
    for j in range(N):
        if l[j] != 0:
            sharks[l[j]-1] = [i, j]

dirs = list(map(int, input().split()))
for i in range(M):
    sharks[i].append(dirs[i]-1)

# 각 상어의 우선순위
# 접근 방식은 상어의 인덱스 -> 상어의 방향 -> 우선순위
sharkDirections = []
for _ in range(M):
    sharkDir = []
    for _ in range(4):
        d = [i-1 for i in list(map(int, input().split()))]
        sharkDir.append(d)

    sharkDirections.append(sharkDir)

# 상어 목록 (상어 번호, x, y, 방향)
sharkDeq = deque(tuple([i] + sharks[i] for i in range(M)))

# 냄새가 남은 위치의 set
sharkSmellSets = [set() for _ in range(M)]

sharkSmellMatrix = [[0] * N for _ in range(N)]

for shark in sharkDeq:
    idx, x, y, _ = shark
    sharkSmellSets[idx].add((x, y))
    sharkSmellMatrix[x][y] = K

# 시간
time = 0

while True:
    if len(sharkDeq) == 1:
        print(time)
        break

    if time >= 1000 and len(sharkDeq) > 1:
        print(-1)
        break

    newShark = []

    while sharkDeq:
        idx, x, y, dir = sharkDeq.popleft()

        notSmells = [[-1, -1] for _ in range(4)]
        mySmells = [[-1, -1] for _ in range(4)]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                # 아무 냄새가 없는 칸인지 체크
                if sharkSmellMatrix[nx][ny] == 0:
                    notSmells[i] = [nx, ny]

                # 자신의 냄새가 있는 칸인지 체크
                if (nx, ny) in sharkSmellSets[idx]:
                    mySmells[i] = [nx, ny]

        # 우선순위
        rank = sharkDirections[idx][dir]

        nextX, nextY, nextDir = -1, -1, -1

        for r in rank:
            if nextX != -1 and nextY != -1:
                break
            notSmellX, notSmellY = notSmells[r]
            nextX, nextY = notSmellX, notSmellY
            nextDir = r

        for r in rank:
            if nextX != -1 and nextY != -1:
                break
            mySmellX, mySmellY = mySmells[r]
            nextX, nextY = mySmellX, mySmellY
            nextDir = r

        newShark.append((idx, nextX, nextY, nextDir))

    newSharkList = [[list() * N for _ in range(N)] for _ in range(N)]
    for new in newShark:
        idx, nx, ny, _ = new
        newSharkList[nx][ny].append(idx)

    removableSharks = set()
    for i in range(N):
        for j in range(N):
            if len(newSharkList[i][j]) > 1:
                minShark = min(newSharkList[i][j])
                for index in newSharkList[i][j]:
                    if minShark < index:
                        removableSharks.add(index)

    for i in range(N):
        for j in range(N):
            if sharkSmellMatrix[i][j] != 0:
                sharkSmellMatrix[i][j] -= 1
            if sharkSmellMatrix[i][j] == 0:
                for idx in range(M):
                    sharkSmellSets[idx].discard((i, j))

    newSharkDeq = deque()
    for new in newShark:
        idx, nx, ny, dir = new
        if idx in removableSharks:
            continue
        newSharkDeq.append((idx, nx, ny, dir))
        sharkSmellSets[idx].add((nx, ny))
        sharkSmellMatrix[nx][ny] = K

    sharkDeq = newSharkDeq
    time += 1

