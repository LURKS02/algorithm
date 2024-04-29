import math

n = int(input())
dp = [50001] * (n + 1)

count = 0

bign = math.floor(math.sqrt(n))

dp[1] = 1
if n >= 2:
    dp[2] = 2

for i in range(1, bign + 1):
    dp[pow(i, 2)] = 1
if n >= 3:
    for i in range(3, n+1):
        j = 1
        while j * j <= i:
            if dp[i] == 1:
                break
            dp[i] = min(dp[i], dp[i - pow(j,2)] + 1)
            j += 1

print(dp[n])