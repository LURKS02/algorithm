from collections import deque

N = int(input())
map = [list(input()) for _ in range(N)]
doors = []

for i in range(N):
    for j in range(N):
        if map[i][j] == '#':
            doors.append((i, j))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque()
endX = doors[1][0]
endY = doors[1][1]
q.append((doors[0], 0, 0))
q.append((doors[0], 0, 1))
q.append((doors[0], 0, 2))
q.append((doors[0], 0, 3))

while q:
    (x, y), mirrorCount, direction = q.popleft()

    nx = x + dx[direction]
    ny = y + dy[direction]

    while 0 <= nx < N and 0 <= ny < N and map[nx][ny] != '*':
        if map[nx][ny] == '!':
            if direction == 0 or direction == 2:
                q.append(((nx, ny), mirrorCount + 1, 1))
                q.append(((nx, ny), mirrorCount + 1, 3))
            else:
                q.append(((nx, ny), mirrorCount + 1, 0))
                q.append(((nx, ny), mirrorCount + 1, 2))

        if nx == endX and ny == endY:
            q.clear()
            break

        nx += dx[direction]
        ny += dy[direction]

print(mirrorCount)