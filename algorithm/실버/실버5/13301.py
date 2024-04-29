dp = [1, 1]

def getRound(N):
    if N == 1:
        return dp[0]
    elif N == 2:
        return dp[1]
    else:
        for i in range(3, N + 1):
            dp.append(dp[i-2] + dp[i-3])
        return dp[N -1]

N = int(input())
if N == 1:
    print(4)
elif N == 2:
    print(6)
else:
    print(getRound(N) * 3 + getRound(N - 1) * 3 + getRound(N - 2))
