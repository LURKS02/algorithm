N = int(input())
milks = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
added = False

if milks[0][0] == 0:
    dp[0][0][0] = 1

milkDict = {0: 2, 1: 0, 2: 1}

for i in range(N):
    for j in range(N):
        currentMilk = milks[i][j]
        if i == 0 and j == 0:
            continue
        if i > 0:
            for k in range(3):
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k])
            if currentMilk == 0:
                dp[i][j][0] = max(dp[i][j][0], 1)
            if dp[i-1][j][milkDict[currentMilk]] >= 1:
                dp[i][j][currentMilk] = max(dp[i][j][currentMilk], dp[i-1][j][milkDict[currentMilk]]+1)

        if j > 0:
            for k in range(3):
                dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k])
            if currentMilk == 0:
                dp[i][j][0] = max(dp[i][j][0], 1)
            if dp[i][j-1][milkDict[currentMilk]] >= 1:
                dp[i][j][currentMilk] = max(dp[i][j][currentMilk], dp[i][j-1][milkDict[currentMilk]]+1)

print(max(dp[-1][-1]))