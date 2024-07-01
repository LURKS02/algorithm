import sys
input = sys.stdin.readline

while True:
    N, M = map(float, input().split())
    if N == 0 and M == 0.00:
        break
    N = int(N)

    dp = [0]*(int(M*100+0.5)+1)
    candy = [(0, 0)]

    for _ in range(N):
        a, b = map(float, input().split())
        candy.append((int(a), int(b*100+0.5)))

    for i in range(1, N+1):
        for j in range(1, int(M*100)+1):
            weight = candy[i][1]
            value = candy[i][0]

            if j >= weight:
                dp[j] = max(dp[j-weight]+value, dp[j-1], dp[j])
            else:
                dp[j] = max(dp[j], dp[j-1])

    print(dp[-1])