N, M, K = map(int, input().split())

# dp = [스킬][체력][N번]

skills = []

maxX = 0
for _ in range(N):
    X, Y = map(int, input().split())
    skills.append((X, Y))
    maxX = max(maxX, M // Y)

dp = [[float('inf') for _ in range(M+1)] for _ in range(N+1)]

dp[0][M] = 0

for i in range(1, N+1):
    for j in range(M+1):
        skillMana = skills[i-1][0]
        skillAttack = skills[i-1][1]
        for k in range(0, (j // skillAttack) + 1):
            if k == 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
            elif k == 1:
                dp[i][j-skillAttack] = min(dp[i][j-skillAttack], dp[i-1][j] + skillMana)
            else:
                dp[i][j - skillAttack * k] = min(dp[i][j - skillAttack * k], dp[i][j - skillAttack * (k-1)] + skillMana + K * (k-1))

print(dp[N][0])
