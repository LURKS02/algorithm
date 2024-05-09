N = int(input())
dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1

n = 2
while n < N+1:
    dp[n] = dp[n-1] + dp[n-2] * 2
    n += 1

if N % 2 == 0:
    print((dp[N] + dp[N//2] + 2*dp[(N-2)//2])//2)
else:
    print((dp[N] + dp[(N-1)//2])//2)