T, W = map(int, input().split())

# dp = [시간(단계)][위치][남은 찬스 수]

dp = [[[-float('inf')] * (W+1) for _ in range(2)] for _ in range(T+1)]
dp[0][0][W] = 0

for i in range(T):
    tree = int(input()) - 1
    step = i + 1

    for j in range(2):
        for k in range(W+1):
            if j == tree:
                dp[step][tree][k] = max(dp[step][tree][k], dp[step-1][tree][k] + 1)
            else:
                if k > 0:
                    dp[step][tree][k-1] = max(dp[step][tree][k-1], dp[step-1][j][k] + 1)
                    dp[step][j][k] = max(dp[step][j][k], dp[step-1][j][k])
                else:
                    dp[step][j][k] = max(dp[step][j][k], dp[step-1][j][k])

maxNumber = 0
for i in range(2):
    for k in range(W+1):
        maxNumber = max(maxNumber, dp[T][i][k])

print(maxNumber)


