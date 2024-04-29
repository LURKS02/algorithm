import sys

input = sys.stdin.readline

n = int(input().rstrip())

l = [-1]

for _ in range(n):
    l.append(int(input().rstrip()))

dp = [-1 for _ in range(n + 1)]

dp[1] = l[1]

if n >= 2:
    dp[2] = l[1] + l[2]
if n >= 3:
    dp[3] = max(dp[2], dp[1] + l[3], l[2] + l[3])

    for i in range(4, n+1):
        dp[i] = max(dp[i-1], dp[i-2] + l[i], dp[i-3] + l[i-1] + l[i])

print(max(dp))

