N, M, A, B = map(int, input().split())

matrix = [[0] * M for _ in range(N)]

for _ in range(A):
    x, y = map(int, input().split())
    matrix[x-1][y-1] = 1

for _ in range(B):
    x, y = map(int, input().split())
    matrix[x-1][y-1] = -1

dp = [[[0] * (A+1) for _ in range(M)] for _ in range(N)]

dp[0][0][0] = 1

for i in range(N):
    for j in range(M):
        for item in range(A+1):
            if matrix[i][j] == 0:
                if i > 0:
                    dp[i][j][item] += dp[i-1][j][item]
                if j > 0:
                    dp[i][j][item] += dp[i][j-1][item]

            elif matrix[i][j] == 1:
                if i > 0 and item > 0:
                    dp[i][j][item] += dp[i - 1][j][item-1]
                if j > 0 and item > 0:
                    dp[i][j][item] += dp[i][j-1][item - 1]

            else:
                continue

print(dp[N-1][M-1][A])