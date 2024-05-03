import sys
sys.setrecursionlimit(600000)

def go(i, j):
    if i < 0 or i >= N or j < 0 or j >= M:
        return 1

    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = 0
    dp[i][j] = max(dp[i][j], go(i + direction[maze[i][j]][0], j + direction[maze[i][j]][1]))
    return dp[i][j]


N, M = map(int, input().split())
maze = [list(input().strip()) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]

direction = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
ans = 0

for i in range(N):
    for j in range(M):
        if dp[i][j] == -1:
            if go(i, j) != 0:
                ans += 1
        elif dp[i][j] == 1:
            ans += 1

print(ans)