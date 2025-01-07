import sys
sys.setrecursionlimit(10**9)

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]

answer = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dp = [[-float('inf')] * N for _ in range(M)]

def dfs(x, y, matrix):
    if dp[x][y] != -float('inf'):
        return dp[x][y]

    if x == M-1 and y == N-1:
        return 1

    dp[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and matrix[nx][ny] < matrix[x][y]:
            dp[x][y] += dfs(nx, ny, matrix)

    return max(dp[x][y], 0)

dfs(0, 0, matrix)
print(dp[0][0])