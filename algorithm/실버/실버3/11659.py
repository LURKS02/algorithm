import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

l = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0]
sum = 0
for num in l:
    sum += num
    dp.append(sum)

for _ in range(M):

    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(dp[j] - dp[i-1])