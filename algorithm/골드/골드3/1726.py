from collections import deque

M, N = map(int, input().split())

board = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(M):
    board.append(list(map(int, input().split())))

startX, startY, startDirection = map(int, input().split())
endX, endY, endDirection = map(int, input().split())

visited = [[[False] * 4 for _ in range(N)] for _ in range(M)]

deq = deque()
deq.append((0, startX-1, startY-1, startDirection-1))
visited[startX-1][startY-1][startDirection-1] = True

while deq:
    count, x, y, direction = deq.popleft()

    if x == endX - 1 and y == endY - 1 and endDirection - 1 == direction:
        print(count)
        break

    for i in range(1, 4):
        nx, ny = x + dx[direction]*i, y + dy[direction]*i
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny][direction]:
            tempX, tempY = x, y
            breakPoint = False
            while not (tempX == nx and tempY == ny):
                tempX += dx[direction]
                tempY += dy[direction]
                if board[tempX][tempY] == 1:
                    breakPoint = True
                    break
            if breakPoint:
                continue

            visited[nx][ny][direction] = True
            deq.append((count+1, nx, ny, direction))

    leftDir, rightDir = -1, -1
    if direction == 0:
        leftDir, rightDir = 3, 2
    elif direction == 1:
        leftDir, rightDir = 2, 3
    elif direction == 2:
        leftDir, rightDir = 0, 1
    else:
        leftDir, rightDir = 1, 0

    if not visited[x][y][leftDir]:
        visited[x][y][leftDir] = True
        deq.append((count+1, x, y, leftDir))

    if not visited[x][y][rightDir]:
        visited[x][y][rightDir] = True
        deq.append((count+1, x, y, rightDir))

