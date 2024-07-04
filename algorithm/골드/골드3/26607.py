N, K, x = map(int, input().split())
abilities = []
for _ in range(N):
    a, b = map(int, input().split())
    abilities.append((a, b))

# K명까지 뽑을 수 있고, a의 합이 j까지 존재
dp = [[-1] * (x*K + 1) for _ in range(K+1)]
dp[0][0] = 0

for a, b in abilities:
    for i in range(K, 0, -1):
        for j in range(x*i, -1, -1):
            if dp[i-1][j] != -1:
                dp[i][j+a] = max(dp[i][j+a], dp[i-1][j] + b)

print(dp)

maxAbility = 0
for j in range(x*K + 1):
    if dp[K][j] != -1:
        maxAbility = max(maxAbility, j * dp[K][j])

print(maxAbility)