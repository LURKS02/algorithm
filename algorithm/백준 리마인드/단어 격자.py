H, W, L = map(int, input().split())

matrix = []

for _ in range(H):
    line = list(input())
    matrix.append(line)

s = list(input())

dp = [[[0] * W for _ in range(H)] for _ in range(L)]

for i in range(H):
    for j in range(W):
        if matrix[i][j] == s[0]:
            dp[0][i][j] = 1

for spot in range(1, L):
    for h in range(H):
        for w in range(W):
            if matrix[h][w] != s[spot]:
                continue

            if h + 1 < H and matrix[h+1][w] == s[spot-1]:
                dp[spot][h][w] += dp[spot-1][h+1][w]
            if w + 1 < W and matrix[h][w+1] == s[spot-1]:
                dp[spot][h][w] += dp[spot-1][h][w+1]
            if h - 1 >= 0 and matrix[h-1][w] == s[spot-1]:
                dp[spot][h][w] += dp[spot-1][h-1][w]
            if w - 1 >= 0 and matrix[h][w-1] == s[spot-1]:
                dp[spot][h][w] += dp[spot-1][h][w-1]
            if h + 1 < H and w + 1 < W and matrix[h+1][w+1] == s[spot-1]:
                dp[spot][h][w] += dp[spot-1][h+1][w+1]
            if h + 1 < H and w - 1 >= 0 and matrix[h+1][w-1] == s[spot-1]:
                dp[spot][h][w] += dp[spot-1][h+1][w-1]
            if h - 1 >= 0 and w + 1 < W and matrix[h-1][w+1] == s[spot-1]:
                dp[spot][h][w] += dp[spot-1][h-1][w+1]
            if h - 1 >= 0 and w - 1 >= 0 and matrix[h-1][w-1] == s[spot-1]:
                dp[spot][h][w] += dp[spot-1][h-1][w-1]

total = 0

for i in range(H):
    for j in range(W):
        total += dp[L-1][i][j]
print(total)
