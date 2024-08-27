import sys
input = sys.stdin.readline

N, K = map(int, input().split())
s = list(map(int, input().split()))
h = list(map(int, input().split()))

dp = [[-float('inf')] * 101 for _ in range(N+1)]
dp[0][100] = 0

for i in range(N):
    for k in range(100, -1, -1):
        if k - h[i] >= 0:
            dp[i+1][min(k - h[i] + K, 100)] = max(dp[i+1][min(k - h[i] + K, 100)], dp[i][k] + s[i])
        dp[i+1][min(k + K, 100)] = max(dp[i+1][min(k + K, 100)], dp[i][k])

# print(dp[1][100])
print(max(dp[N]))