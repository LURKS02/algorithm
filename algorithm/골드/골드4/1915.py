import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = []
dp = [[0] * M for _ in range(N)]

for _ in range(N):
    board.append(list(map(int, list(input().rstrip()))))

answer = 0
for i in range(N):
    for j in range(M):
        if i == 0 or j == 0:
            dp[i][j] = board[i][j]
        elif board[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        answer = max(dp[i][j], answer)

print(answer*answer)
