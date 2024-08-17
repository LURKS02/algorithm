import heapq

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
startLevel = matrix[0][0]

heap = []
heap.append((startLevel, 0, 0, 0))
cost = [[[float('inf')] * 2 for _ in range(M)] for _ in range(N)]
cost[0][0][0] = startLevel

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while heap:
    level, usedChance, x, y = heapq.heappop(heap)

    if x == N-1 and y == M-1:
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if usedChance == 0:
                nextX, nextY = nx + dx[i], ny + dy[i]
                if 0 <= nextX < N and 0 <= nextY < M:
                    newLevel = max(level, matrix[nextX][nextY])
                    if newLevel < cost[nextX][nextY][1]:
                        cost[nextX][nextY][1] = newLevel
                        heapq.heappush(heap, (newLevel, 1, nextX, nextY))

                newLevel = max(level, matrix[nx][ny])
                if newLevel < cost[nx][ny][0]:
                    cost[nx][ny][0] = newLevel
                    heapq.heappush(heap, (newLevel, 0, nx, ny))

            else:
                newLevel = max(level, matrix[nx][ny])
                if newLevel < cost[nx][ny][1]:
                    cost[nx][ny][1] = newLevel
                    heapq.heappush(heap, (newLevel, 1, nx, ny))

print(min(cost[N-1][M-1]))