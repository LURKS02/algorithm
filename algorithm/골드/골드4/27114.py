A, B, C, K = map(int, input().split())

dp = [float('inf')] * (K+1)

energy = []
# 좌*4
energy.append((A*4, 4))
# 우*4
energy.append((B*4, 4))
# 좌*2 + 뒤
energy.append((A*2+C, 3))
# 우*2 + 뒤
energy.append((B*2+C, 3))
# 좌 + 우
energy.append((A+B, 2))
# 뒤*2
energy.append((C*2, 2))
# 좌*3 + 뒤*1 + 우*1
energy.append((A*3+B+C, 5))
# 좌*1 + 우*3 + 뒤*1
energy.append((A+B*3+C, 5))

dp[0] = 0

for en, count in energy:
    for i in range(K+1):
        if i >= en:
            dp[i] = min(dp[i], dp[i-en]+count)

print(dp[K]) if dp[K] != float('inf') else print(-1)

