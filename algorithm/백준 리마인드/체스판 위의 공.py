R, C = map(int, input().split())
matrix = []

position = dict()

for _ in range(R):
    line = list(map(int, input().split()))
    matrix.append(line)

for i in range(R):
    for j in range(C):
        num = matrix[i][j]
        position[num] = (i, j)

dp = [[1] * C for _ in range(R)]

dx = [0, 0, -1, -1, -1, 1, 1, 1]
dy = [1, -1, 0, 1, -1, 0, 1, -1]

for key in range(300000, -1, -1):
    if key in position:
        px, py = position[key]

        tx, ty = -1, -1
        minValue = key

        for i in range(8):
            nx, ny = px + dx[i], py + dy[i]

            if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] < minValue:
                minValue = matrix[nx][ny]
                tx, ty = nx, ny

        if tx == -1 and ty == -1:
            continue

        else:
            dp[tx][ty] += dp[px][py]
            dp[px][py] = 0

for i in range(R):
    print(*dp[i])


