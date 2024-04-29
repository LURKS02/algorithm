from collections import deque

dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

M, N, H = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque([])

for h in range(H):
    for n in range(N):
        for m in range(M):
            if matrix[h][n][m] == 1:
                queue.append((h, n, m, 0))

max_days = 0
while queue:
    z, y, x, days = queue.popleft()
    max_days = max(max_days, days)
    for i in range(6):
        nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and matrix[nz][ny][nx] == 0:
            matrix[nz][ny][nx] = 1
            queue.append((nz, ny, nx, days + 1))

if any(0 in row for layer in matrix for row in layer):
    print(-1)
else:
    print(max_days)
