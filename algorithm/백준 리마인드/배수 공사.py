import sys

line1 = list(map(int, sys.stdin.readline().split()))
N, x = line1[0], line1[1]

pipes = []

for _ in range(N):
    line2 = list(map(int, sys.stdin.readline().split()))
    L, C = line2[0], line2[1]
    pipes.append([L, C])

dp = [0] * (x + 1)
dp[0] = 1

for i in range(N):
    pipe = pipes[i][0]
    pipeNumber = pipes[i][1]

    for j in range(x, -1, -1):
        for k in range(pipeNumber, 0, -1):
            if j >= pipe * k:
                dp[j] += dp[j - pipe * k]

print(dp[x])