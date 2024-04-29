import sys
input = sys.stdin.readline

maps = []

N, M = map(int, input().rstrip().split())

for _ in range(N):
    maps.append(list(map(int, input().rstrip().split())))

dp = [[-float('inf')] * M for _ in range(N)]

dp[0][0] = maps[0][0]

for i in range(1, M):
    dp[0][i] = dp[0][i-1] + maps[0][i]

for i in range(1, N):
    l1 = [-float('inf')] * M
    l1[0] = dp[i-1][0] + maps[i][0]

    for j in range(1, M):
        l1[j] = max(dp[i-1][j], l1[j-1]) + maps[i][j]

    l2 = [-float('inf')] * M
    l2[-1] = dp[i-1][-1] + maps[i][-1]

    for j in range(M-2, -1, -1):
        l2[j] = max(dp[i-1][j], l2[j+1]) + maps[i][j]

    for j in range(M):
        dp[i][j] = max(l1[j], l2[j])

print(dp[N-1][M-1])