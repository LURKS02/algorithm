# 색상의 수
N = int(input())
# 선택한 수
K = int(input())

MOD = 1000000003

# 첫 번째 색상을 뽑을 경우
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(N + 1):
    dp[i][0] = 1
    dp[i][1] = i

for i in range(2, N + 1):
    for j in range(2, K + 1):
        if i == N:
            dp[i][j] = (dp[i-1][j] + dp[i-3][j-1]) % MOD
        else:
            dp[i][j] = (dp[i-1][j] + dp[i-2][j-1]) % MOD

print(dp[N][K])