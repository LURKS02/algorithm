N = int(input())
currentList = list(map(int, input().split()))
targetList = list(map(int, input().split()))

diffList = [targetList[i] - currentList[i] for i in range(N)]

dp = [0] * N
dp[0] = abs(diffList[0])

for i in range(1, N):
    if diffList[i] * diffList[i-1] > 0:
        dp[i] = dp[i-1] + max(0, abs(diffList[i]) - abs(diffList[i-1]))
    else:
        dp[i] = dp[i-1] + abs(diffList[i])

print(dp[-1])