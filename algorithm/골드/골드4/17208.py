# N = 주문의 수
# M = 치즈버거 개수
# K = 감자튀김 개수
N, M, K = map(int, input().split())

# (치즈버거, 감자튀김) 주문 목록
orders = []

for _ in range(N):
    # x = 치즈버거 요구 개수
    # y = 감자튀김 요구 개수
    x, y = map(int, input().split())
    orders.append((x, y))

# dp = [치즈버거][감자튀김] = 주문 개수

dp = [[0] * (K+1) for _ in range(M+1)]

for cheese, potato in orders:
    for i in range(M, cheese-1, -1):
        for j in range(K, potato-1, -1):
            dp[i][j] = max(dp[i][j], dp[i - cheese][j - potato] + 1)

print(dp[M][K])