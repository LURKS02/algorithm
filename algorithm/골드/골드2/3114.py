R, C = map(int, input().split())
grid = [input().split() for _ in range(R)]

inpA = [[0] * (C+1) for _ in range(R+1)]
inpB = [[0] * (C+1) for _ in range(R+1)]
dp = [[0] * (C+1) for _ in range(R+1)]

for i in range(1, R+1):
    for j in range(1, C+1):
        c = grid[i-1][j-1][0]
        t = grid[i-1][j-1][1:]
        t = int(t)

        if c == "A":
            inpA[i][j] = t
        else:
            inpB[i][j] = t

for i in range(1, R+1):
    for j in range(1, C+1):
        inpA[i][j] += inpA[i-1][j]
        inpB[i][j] += inpB[i-1][j]

for i in range(1, R+1):
    for j in range(1, C+1):
        if j == 1:
            dp[i][j] = inpA[R][1] - inpA[i][j]
        else:
            val = (inpA[R][j] - inpA[i][j]) + inpB[i-1][j]
            dp[i][j] = max(dp[i-1][j-1] + val, max(dp[i][j-1] + val, dp[i-1][j] - (inpA[i][j] - inpA[i-1][j])))

print(dp[R][C])