from collections import deque
import sys

sys.setrecursionlimit(10**9)

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N or board[y][x] == 'H':
        return 0
    if visited[y][x]:
        print(-1)
        exit(0)
    if dp[y][x] != 0:
        return dp[y][x]

    visited[y][x] = True
    for i in range(4):
        nx, ny = x + dx[i] * int(board[y][x]), y + dy[i] * int(board[y][x])
        dp[y][x] = max(dp[y][x], dfs(nx, ny) + 1)
    visited[y][x] = False

    return dp[y][x]

print(dfs(0, 0))

# for i in range(N):
#     print(*dp[i])