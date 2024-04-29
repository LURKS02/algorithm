def max_volume(N, S, M, V):
    dp = [[False] * (M + 1) for _ in range(N + 1)]
    dp[0][S] = True

    for i in range(1, N + 1):
        for j in range(M + 1):
            if dp[i-1][j]:
                if j - V[i-1] >= 0:
                    dp[i][j - V[i-1]] = True
                if j + V[i-1] <= M:
                    dp[i][j + V[i-1]] = True

    for i in range(M, -1, -1):
        if dp[N][i]:
            return i
    return -1

N, S, M = map(int, input().split())
V = list(map(int, input().split()))

print(max_volume(N, S, M, V))