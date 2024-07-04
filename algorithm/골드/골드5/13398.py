N = int(input())
l = list(map(int, input().split()))
dp = [[0] * N for _ in range(2)]

dp[0][0] = l[0]

if N != 1:
    ans = -1e9
    for i in range(1, N):
        dp[0][i] = max(dp[0][i-1] + l[i], l[i])
        dp[1][i] = max(dp[0][i-1], dp[1][i-1] + l[i])

        ans = max(ans, dp[0][i], dp[1][i])

    print(ans)

else:
    print(dp[0][0])