n = int(input())

l = list(map(int, input().split()))

dp = []

for i in range(len(l)):
    if i == 0:
        dp.append(l[i])
    else:
        dp.append(max(dp[i - 1] + l[i], l[i]))
print(max(dp))