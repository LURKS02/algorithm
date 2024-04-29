n = int(input())
l = list(map(int, input().split()))

dp = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[i] = 1
    else:
        dp[i] = max((dp[k] + 1 for k in range(i) if l[k] < l[i]), default=1)

print(max(dp))