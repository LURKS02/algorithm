magicWord = list(input())

devil = list(input())
angel = list(input())

# dp = [마법 단어 위치][고려한 다리 글자 수][악마/천사]
dp = [[[0] * 2 for _ in range(len(devil))] for _ in range(len(magicWord))]

for j in range(len(devil)):
    if devil[j] == magicWord[0]:
        dp[0][j][0] = 1
    if angel[j] == magicWord[0]:
        dp[0][j][1] = 1

for i in range(1, len(magicWord)):
    for j in range(len(devil)):
        if devil[j] == magicWord[i]:
            for k in range(j):
                dp[i][j][0] += dp[i-1][k][1]
        if angel[j] == magicWord[i]:
            for k in range(j):
                dp[i][j][1] += dp[i-1][k][0]

devilSum = sum(dp[len(magicWord)-1][i][0] for i in range(len(devil)))
angelSum = sum(dp[len(magicWord)-1][i][1] for i in range(len(devil)))
print(devilSum + angelSum)