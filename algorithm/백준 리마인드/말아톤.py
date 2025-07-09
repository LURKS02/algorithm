import sys
input = sys.stdin.readline

H, N = map(int, input().split())

dp = [-float('inf')] * (H+1)
dp[0] = float('inf')

for _ in range(N):
    h, s = map(int, input().split())

    if h > H:
        continue

    for i in range(H, -1, -1):
        if i >= h:
            dp[i] = max(dp[i], min(dp[i-h], s))
        else:
            break

print(dp[H])