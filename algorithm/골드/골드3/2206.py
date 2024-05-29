import heapq

N, M = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

board = [list(map(int, list(input()))) for _ in range(N)]

heap = []
distance = [[float('inf')] * M for _ in range(N)]
heapq.heappush(heap, (0, 0, 0, 0))
distance[0][0] = 0

while heap:
    count, breaks, x, y = heapq.heappop(heap)

    if distance[x][y] < breaks:
        continue

    if x == N-1 and y == M-1:
        print(count + 1)
        exit(0)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 1:
                newBreaks = breaks + 1
                if newBreaks < 2 and distance[nx][ny] > newBreaks:
                    distance[nx][ny] = newBreaks
                    heapq.heappush(heap, (count+1, newBreaks, nx, ny))
            else:
                newBreaks = breaks
                if newBreaks < 2 and distance[nx][ny] > newBreaks:
                    distance[nx][ny] = newBreaks
                    heapq.heappush(heap, (count+1, newBreaks, nx, ny))

print(-1)