N, M = map(int, input().split())

matrix = [list(input()) for _ in range(N)]

dots = set()
for i in range(N):
    for j in range(M):
        if matrix[i][j] == '*':
            dots.add((i, j))

if len(dots) == 0:
    print(-1)
    exit(0)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

targets = []

for x in range(N):
    for y in range(M):
        if matrix[x][y] == '*':
            idx = 0
            while True:
                idx += 1
                removable = []
                for i in range(4):
                    nx, ny = x + idx * dx[i], y + idx * dy[i]
                    if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == '*':
                        removable.append((nx, ny))

                if len(removable) == 4:
                    for (tx, ty) in removable:
                        if (tx, ty) in dots:
                            dots.remove((tx, ty))
                else:
                    idx -= 1
                    break

            if idx != 0:
                if (x, y) in dots:
                    dots.remove((x, y))
                targets.append((x, y, idx))

if len(dots) == 0:
    print(len(targets))
    for x, y, idx in targets:
        print(x+1, y+1, idx)

else:
    print(-1)