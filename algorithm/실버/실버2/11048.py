N, M = map(int, input().split())

l = []
for _ in range(N):
    newl = list(map(int, input().split()))
    l.append(newl)

dp = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i - 1 >= 0 and j - 1 >= 0:
            dp[i][j] = max(dp[i-1][j] + l[i][j], dp[i][j-1] + l[i][j], dp[i-1][j-1] + l[i][j])
        elif i-1 >= 0:
            dp[i][j] = dp[i-1][j] + l[i][j]
        elif j-1 >= 0:
            dp[i][j] = dp[i][j-1] + l[i][j]
        else:
            dp[i][j] = l[i][j]

print(dp[N-1][M-1])