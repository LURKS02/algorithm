N = int(input())
a = list(map(int, input().split()))
maxHam = sum(a)

# A가 얻는 효용 + B가 얻는 효용 = C가 얻는 효용
dp = [[-1] * (maxHam+1) for _ in range(maxHam+1)]

dp[0][0] = 0

for ham in a:
    for i in range(maxHam, -1, -1):
        for j in range(maxHam, -1, -1):
            if dp[i][j] != -1:
                if i+ham <= maxHam:
                    dp[i+ham][j] = max(dp[i+ham][j], dp[i][j])
                if j+ham <= maxHam:
                    dp[i][j+ham] = max(dp[i][j+ham], dp[i][j])
                dp[i][j] += ham

maxValue = 0
for i in range(maxHam+1):
    for j in range(maxHam+1):
        if dp[i][j] != -1:
            K = maxHam - i - j
            if K >= 0 and i >= K and j >= K:
                maxValue = max(maxValue, K)

print(maxValue)

