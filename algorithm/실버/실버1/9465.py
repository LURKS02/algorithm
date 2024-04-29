T = int(input())

for _ in range(T):
    n = int(input())
    l = []

    for _ in range(2):
        l.append([0] + list(map(int, input().split())))

    dp = [[0 for _ in range(n+1)] for _ in range(2)]

    dp[0][1] = l[0][1]
    dp[1][1] = l[1][1]

    for i in range(2, n+1):
        dp[0][i] = max(dp[1][i-1] + l[0][i], dp[1][i-2] + l[0][i])
        dp[1][i] = max(dp[0][i-1] + l[1][i], dp[0][i-2] + l[1][i])

    print(max(dp[0][n], dp[1][n]))