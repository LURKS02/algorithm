str1 = list(input())
str2 = list(input())

# dp = [A 위치][B 위치] = 최대 길이

dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

answer = 0

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
            answer = max(answer, dp[i+1][j+1])

print(answer)
