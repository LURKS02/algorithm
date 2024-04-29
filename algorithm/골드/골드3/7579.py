N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
max_cost = sum(costs)

dp = [[0] * (max_cost + 1) for _ in range(N + 1)]
dp[0][0] = 0
ans = sum(costs)

for i in range(1, N + 1):
    memory = memories[i-1]
    cost = costs[i-1]

    for j in range(max_cost + 1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(memory + dp[i-1][j-cost], dp[i-1][j])

        if dp[i][j] >= M:
            ans = min(ans, j)

if M != 0:
    print(ans)
else:
    print(0)