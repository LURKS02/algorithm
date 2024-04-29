N = int(input())

cards = [0] + list(map(int, input().split()))

dp = [0 for _ in range(N + 1)]

dp[1] = cards[1]

for i in range(2, N+1):
    dp[i] = min([cards[i-k] + dp[k] for k in range(0, i)])

print(dp[N])