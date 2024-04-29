N = int(input())

color = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1 for _ in range(3)] for _ in range(N)]

dp[0][0] = color[0][0]
dp[0][1] = 10000000
dp[0][2] = 10000000

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + color[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + color[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + color[i][2]

red = min(dp[N-1][1], dp[N-1][2])

dp[0][0] = 10000000
dp[0][1] = color[0][1]
dp[0][2] = 10000000

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + color[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + color[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + color[i][2]

green = min(dp[N-1][0], dp[N-1][2])

dp[0][0] = 10000000
dp[0][1] = 10000000
dp[0][2] = color[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + color[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + color[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + color[i][2]

blue = min(dp[N - 1][0], dp[N - 1][1])

print(min(red, green, blue))
