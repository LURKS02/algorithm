n = int(input())

dp = [0, 1, 3]

def getNum(N):
    if N == 1:
        return dp[1]
    elif N == 2:
        return dp[2]
    else:
        for i in range(3, N + 1):
            dp.append(dp[i - 1] + dp[i - 2] * 2)
        return dp[N]

print(getNum(n) % 10007)