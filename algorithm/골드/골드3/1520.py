N, M = map(int, input().split())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

dp = [[-1 for _ in range(M)] for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0

    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]

        if 0 <= newX < M and 0 <= newY < N and matrix[y][x] > matrix[newY][newX]:
            dp[y][x] += dfs(newX, newY)

    return dp[y][x]

dfs(0, 0)

print(dp[0][0])