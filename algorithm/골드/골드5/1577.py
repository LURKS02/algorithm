import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())

dp = [[0] * (M+1) for _ in range(N+1)]
dp[0][0] = 1

end = set()
loads = set()

for _ in range(K):
    a, b, c, d = map(int, input().split())
    (a, b), (c, d) = sorted([(a, b), (c, d)])
    end.add((c, d))
    loads.add((a, b, c, d))

for i in range(N+1):
    for j in range(M+1):
        if i == 0 and j == 0: continue

        if (i, j) in end:
            if (i, j-1, i, j) in loads and (i-1, j, i, j) not in loads:
                dp[i][j] = dp[i-1][j]
            if (i-1, j, i, j) in loads and (i, j-1, i, j) not in loads:
                dp[i][j] = dp[i][j-1]

        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[N][M])