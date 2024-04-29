from collections import deque

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

startX = -1
startY = -1

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            startX, startY = j, i
            matrix[startY][startX] = 0
            break

size = 2
time = 0

def bfs(startX, startY):
    deq = deque()
    deq.append((startX, startY))

    dist = [[-1 for _ in range(N)] for _ in range(N)]
    dist[startY][startX] = 0
    fish = []

    while(deq):
        currentX, currentY = deq.popleft()

        for i in range(4):
            newX = currentX + dx[i]
            newY = currentY + dy[i]

            if 0 <= newX < N and 0 <= newY < N and dist[newY][newX] == -1 and matrix[newY][newX] <= size:
                dist[newY][newX] = dist[currentY][currentX] + 1
                deq.append((newX, newY))
                if 0 < matrix[newY][newX] < size:
                    fish.append((dist[newY][newX], newX, newY))

    if fish:
        fish.sort(key=lambda x: (x[0], x[2], x[1]))
        return fish[0][1], fish[0][2], fish[0][0]

    else:
        return -1, -1, -1

eat = 0
time = 0
while True:
    x, y, dist = bfs(startX, startY)
    if x == -1: break  # 먹을 수 있는 물고기가 없으면 종료
    startX, startY = x, y
    matrix[y][x] = 0  # 물고기 먹기
    time += dist  # 이동 시간 더하기
    eat += 1
    if eat == size:  # 크기만큼 먹으면 크기 증가
        size += 1
        eat = 0

print(time)