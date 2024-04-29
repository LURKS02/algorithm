dp = [0, 1]

n = int(input())



def fibo(n):
    if n == 0:
        return dp[0]
    elif n == 1:
        return dp[1]
    else:
        for i in range(2, n + 1):
            dp.append(dp[i - 2] + dp[i - 1])

        return dp[n]

print(fibo(n))
