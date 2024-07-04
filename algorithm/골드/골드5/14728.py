import sys
input = sys.stdin.readline

N, T = map(int, input().split())

lectures = []

for _ in range(N):
    t, s = map(int, input().split())
    lectures.append((t, s))

dp = [[0] * (T+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, T+1):
        if j >= lectures[i-1][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-lectures[i-1][0]] + lectures[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][T])