import sys
input = sys.stdin.readline

N = int(input().rstrip())

tasks = []

for _ in range(N):
    a, b = map(int, input().rstrip().split())
    tasks.append((a, b))

maxTime = sum(max(a, b) for a, b in tasks)
dp = [[float('inf')] * (maxTime+1) for _ in range(N+1)]
dp[0][0] = 0

minTime = float('inf')
for i in range(1, N+1):
    a, b = tasks[i-1]
    for j in range(maxTime+1):
        if j >= a:
            dp[i][j] = min(dp[i-1][j-a], dp[i-1][j] + b)
        else:
            dp[i][j] = dp[i-1][j] + b

        if i == N:
            minTime = min(minTime, max(j, dp[i][j]))

print(minTime)