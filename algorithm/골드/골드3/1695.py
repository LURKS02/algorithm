N = int(input())
seq = list(map(int, input().split()))

dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        if seq[i] == seq[-j-1]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

print(N - dp[N][N])
