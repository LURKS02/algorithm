import sys
input = sys.stdin.readline

dp = [0 for _ in range(1000000 + 1)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

limit = 3

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())

    if dp[n] != 0:
        print(dp[n])
    else:
        if limit < n:
            for i in range(limit+1, n+1):
                dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009
            limit = n
        print(dp[n])
