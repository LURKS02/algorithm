N = int(input())
l = list(map(int, input().split()))

dp = [0 for _ in range(len(l))]

for i in range(len(l) - 1, -1, -1):
    if i == len(l) - 1:
        dp[i] = 1
    else:
        dp[i] = max((1 + dp[k] for k in range(i + 1, len(l)) if l[i] > l[k]), default=1)

print(max(dp))