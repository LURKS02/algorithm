N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]

dp[0][1][0] = 1

for r in range(0, N):
    for c in range(1, N):
        if r == 0 and c == 1:
            continue
        if c > 0 and house[r][c-1] == 0 and house[r][c] == 0:
            dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2]
        if r > 1 and c > 0 and house[r-1][c] == 0 and house[r][c] == 0:
            dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2]
        if r > 0 and c > 0 and house[r-1][c] == 0 and house[r][c-1] == 0 and house[r][c] == 0:
            dp[r][c][2] = dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]

print(sum(dp[N-1][N-1]))