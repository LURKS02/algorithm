T = int(input())

dp = [0, 1, 1, 1, 2, 2]

def getNum(N):
    if len(dp) > N:
        return dp[N]
    else:
        for i in range(len(dp), N + 1):
            dp.append(dp[i - 5] + dp[i - 1])
        return dp[N]

for _ in range(T):
    N = int(input())

    print(getNum(N))

