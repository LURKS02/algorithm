str1 = list(input())
str2 = list(input())

dp = [[-float('inf')] * (len(str2)+1) for _ in range(len(str1)+1)]

dp[0][0] = 0
for i in range(len(str1)+1):
    dp[i][0] = 0
for j in range(len(str2)+1):
    dp[0][j] = 0

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
        else:
            dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])

print(dp[len(str1)][len(str2)])