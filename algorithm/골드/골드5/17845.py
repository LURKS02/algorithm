# N = 최대 공부시간 (10,000)
# K = 과목 수 (1,000)
N, K = map(int, input().split())

plans = []

for _ in range(K):
    # I = 중요도 (100,000)
    # T = 필요 공부 시간 (10,000)
    I, T = map(int, input().split())
    plans.append((I, T))

dp = [-float('inf')] * (N+1)
dp[0] = 0

for plan in plans:
    I = plan[0]
    T = plan[1]

    for i in range(N, T-1, -1):
        dp[i] = max(dp[i], dp[i-T] + I)

# print(dp)
print(max(dp))

