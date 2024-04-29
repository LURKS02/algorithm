reccount = 0
dpcount = 0

def recfibo(n):
    global reccount
    if n == 1 or n == 2:
        reccount += 1
        return 1
    else:
        return recfibo(n - 1) + recfibo(n - 2)

def dpfibo(n):
    global dpcount
    dp = [0] * n
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
        dpcount += 1
    return dp[n - 1]


N = int(input())

print(dpfibo(N), dpcount, end= ' ')