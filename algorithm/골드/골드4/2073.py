D, P = map(int, input().split())

# (길이, 용량) 배열
pipes = []

for _ in range(P):
    L, C = map(int, input().split())
    pipes.append((L, C))

# [수도관 용량] * 수도관 길이
dp = [0] * (D + 1)

for length, pool in pipes:
    for i in range(D, length-1, -1):
        dp[i] = max(dp[i], min(pool, dp[i - length]))
    if pool > dp[length]:
        dp[length] = pool

print(dp[D])