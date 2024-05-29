from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m = map(int, input().rstrip().split())
board = []
temp = []

for i in range(n):
    board.append(list(input().rstrip()))
    for j in range(m):
        if board[i][j] == 'o':
            temp.append((i, j))

def bfs():
    coin = deque()
    coin.append((temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0))

    while coin:
        x1, y1, x2, y2, cnt = coin.popleft()

        if cnt >= 10:
            return -1

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]

            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                if board[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1
                if board[nx2][ny2] == '#':
                    nx2, ny2 = x2, y2

                coin.append((nx1, ny1, nx2, ny2, cnt + 1))

            elif 0 <= nx1 < n and 0 <= ny1 < m:
                return cnt + 1

            elif 0 <= nx2 < n and 0 <= ny2 < m:
                return cnt + 1

            else:
                continue

    return -1

print(bfs())