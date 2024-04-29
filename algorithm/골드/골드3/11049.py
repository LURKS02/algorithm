import sys
input = sys.stdin.readline


N = int(input().rstrip())

matrixs = []

for _ in range(N):
    matrixs.append((tuple(map(int, input().rstrip().split()))))

dp = [[0 for _ in range(N)] for _ in range(N)]

for l in range(2, N + 1):
    for i in range(N - l + 1):
        j = i + l - 1
        dp[i][j] = float('inf')

        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + matrixs[i][0] * matrixs[k][1] * matrixs[j][1]
            if cost < dp[i][j]:
                dp[i][j] = cost

print(dp[0][N-1])