N, M, K = map(int, input().split())

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(M + 1):
        if i == 0 or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

if dp[N][M] < K:
    print(-1)

else:
    result = ""
    while N > 0 and M > 0:
        if K <= dp[N-1][M]:
            result += "a"
            N -= 1
        else:
            result += "z"
            K -= dp[N-1][M]
            M -= 1

    result += "a" * N
    result += "z" * M

    print(result)

