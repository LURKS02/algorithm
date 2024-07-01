T, W = map(int, input().split())

inputList = []

for _ in range(T):
    inputList.append(int(input()))

dp = [[0] * (W+1) for _ in range(T+1)]

for i in range(1, W+1):
    dp[0][i] = -float('inf')

for i in range(1, T+1):
    for j in range(0, W+1):
        if (inputList[i-1] == 2 and j % 2 == 1) or (inputList[i-1] == 1 and j % 2 == 0):
            if j > 0:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
            else:
                dp[i][j] = dp[i-1][j] + 1
        else:
            if j > 0:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

print(max(dp[T]))