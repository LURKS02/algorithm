import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

dp = [[float('inf')] * N for _ in range(N)]

dp[0][0] = 0

for i in range(1, N):
    if matrix[0][i-1] > matrix[0][i]:
        dp[0][i] = dp[0][i-1]
    else:
        temp = matrix[0][i] - matrix[0][i-1] + 1
        dp[0][i] = dp[0][i-1] + temp

for i in range(1, N):
    if matrix[i-1][0] > matrix[i][0]:
        dp[i][0] = dp[i-1][0]
    else:
        temp = matrix[i][0] - matrix[i-1][0] + 1
        dp[i][0] = dp[i-1][0] + temp

for i in range(1, N):
    for j in range(1, N):
        # 왼쪽에서 오는 경우
        leftTemp = float('inf')
        if matrix[i][j-1] > matrix[i][j]:
            leftTemp = dp[i][j-1]
        else:
            leftTemp = dp[i][j-1] + matrix[i][j] - matrix[i][j-1] + 1

        # 위에서 오는 경우
        upTemp = float('inf')
        if matrix[i-1][j] > matrix[i][j]:
            upTemp = dp[i-1][j]
        else:
            upTemp = dp[i-1][j] + matrix[i][j] - matrix[i-1][j] + 1

        dp[i][j] = min(leftTemp, upTemp)

print(dp[N-1][N-1])