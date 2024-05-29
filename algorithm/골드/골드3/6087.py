import heapq

# W x H = 100 x 100
W, H = map(int, input().split())
board = [list(input()) for _ in range(H)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

CList = []

for i in range(H):
    for j in range(W):
        if board[i][j] == 'C':
            CList.append((i, j))

startX, startY = CList[0]
endX, endY = CList[1]

heap = []
distances = [[float('inf')] * W for _ in range(H)]
distances[startX][startY] = 0
checks = [[[False] * W for _ in range(H)] for _ in range(2)]

for i in range(4):
    nx, ny = startX + dx[i], startY + dy[i]
    if 0 <= nx < H and 0 <= ny < W and board[nx][ny] != '*':
        distances[nx][ny] = 0
        heapq.heappush(heap, (0, i, nx, ny))

while heap:
    count, direction, x, y = heapq.heappop(heap)

    if distances[x][y] < count:
        continue

    if x == endX and y == endY:
        print(count)
        break

    for i in range(4):
        while True:
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < H and 0 <= ny < W:
                if board[nx][ny] == '.':
                    if distances[nx][ny] > count or (distances[nx][ny] == count and checks[i % 2][nx][ny] == False):
                        distances[nx][ny] = count
                        checks[i % 2][nx][ny] = True

                        heapq.heappush(heap, (count, i, nx, ny))
                        x, y = nx, ny

                    else:
                        break
                if board[nx][ny] == '*':
                    break
                if board[nx][ny] == 'C':
                    print(count)
                    exit(0)

            else:
                break