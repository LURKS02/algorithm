N = int(input())
house = []

for _ in range(N):
    house.append(list(map(int, input().split())))

dp = [[[0]*3 for _ in range(N)] for _ in range(N)]

# 0: 가로
# 1: 세로
# 2: 대각선

dp[0][1][0] = 1

for r in range(N):
    for c in range(2, N):
        if house[r][c] == 0 and house[r][c-1] == 0:
            dp[r][c][0] += dp[r][c-1][0] + dp[r][c-1][2]
        if r > 0 and house[r][c] == 0 and house[r-1][c] == 0:
            dp[r][c][1] += dp[r-1][c][1] + dp[r-1][c][2]
        if r > 0 and house[r][c] == 0 and house[r-1][c] == 0 and house[r][c-1] == 0 and house[r-1][c-1] == 0:
            dp[r][c][2] += dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]

print(sum(dp[N-1][N-1]))