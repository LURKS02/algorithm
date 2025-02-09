import sys
sys.setrecursionlimit(10**9)

M, N = map(int, input().split())

metrix = [list(map(int, input().split())) for _ in range(M)]
dp = [[float('inf')] * N for _ in range(M)]

visited = [[False] * N for _ in range(M)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y, visited):
    if dp[x][y] != float('inf'):
        return dp[x][y]

    if x == M-1 and y == N-1:
        return 1


    dp[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and metrix[x][y] > metrix[nx][ny]:
            visited[nx][ny] = True
            dp[x][y] += dfs(nx, ny, visited)
            visited[nx][ny] = False

    return dp[x][y]

print(dfs(0, 0, visited))

