import sys
sys.setrecursionlimit(10**9)

N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * N for _ in range(N)]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y):
    # print(x, y)
    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 1
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < N:
            if forest[ny][nx] > forest[y][x]:
                dp[y][x] = max(dp[y][x], dfs(nx, ny) + 1)
    return dp[y][x]

max_length = 0
for i in range(N):
    for j in range(N):
        if dp[i][j] == -1:
            max_length = max(max_length, dfs(j, i))
print(max_length)