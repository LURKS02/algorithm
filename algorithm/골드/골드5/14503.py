from collections import deque

N, M = map(int, input().split())

r, c, d = map(int, input().split())

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

deq = deque()
deq.append((r, c, d))

cnt = 0

while deq:
    x, y, dir = deq.popleft()

    if board[x][y] == 0:
        board[x][y] = 2
        cnt += 1

    nearCleaned = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
            nearCleaned = False

    if nearCleaned:
        nx, ny = x + dx[dir]*(-1), y + dy[dir]*(-1)
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 1:
            deq.append((nx, ny, dir))
        else:
            print(cnt)
            break

    else:
        newDir = (dir - 1 + 4) % 4
        nx, ny = x + dx[newDir], y + dy[newDir]

        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
            deq.append((nx, ny, newDir))
        else:
            deq.append((x, y, newDir))