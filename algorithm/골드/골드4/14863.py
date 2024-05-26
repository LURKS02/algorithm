# N = 도시의 개수 (100)
# K = 최대 시간 (100,000)
N, K = map(int, input().split())

# (시간, 모금액)
walk = []
bike = []

for _ in range(N):
    walkTime, walkPay, bikeTime, bikePay = map(int, input().split())
    walk.append((walkTime, walkPay))
    bike.append((bikeTime, bikePay))

# print(biggestTime)

dp = [[-float('inf')] * (K+1) for _ in range(N+1)]

for i in range(K+1):
    dp[0][i] = 0

for i in range(N):
    walkTime, walkPay = walk[i]
    bikeTime, bikePay = bike[i]

    for j in range(K, walkTime - 1, -1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j - walkTime] + walkPay)
    # print(dp)

    for j in range(K, bikeTime - 1, -1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j - bikeTime] + bikePay)
    # print(dp)

maxValue = 0

for i in range(K+1):
    maxValue = max(maxValue, dp[N][i])
print(maxValue)