# N = 남자의 수 (1,000)
# M = 여자의 수 (1,000)
N, M = map(int, input().split())

men = list(map(int, input().split()))
women = list(map(int, input().split()))

men.sort()
women.sort()

dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j-1] + abs(men[i-1]-women[j-1])

        if i > j:
            dp[i][j] = min(dp[i][j], dp[i-1][j])
        elif i < j:
            dp[i][j] = min(dp[i][j], dp[i][j-1])

print(dp[N][M])

