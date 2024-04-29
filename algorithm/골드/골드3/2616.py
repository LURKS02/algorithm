N = int(input())
train = list(map(int, input().split()))
trainLimit = int(input())

def maxPassengers(N, train, trainLimit):
    prefixSum = [0] * (N+1)
    for i in range(1, N+1):
        prefixSum[i] = prefixSum[i-1] + train[i-1]

    # dp[i][j] = i대의 소형 기관차로 j번째 객체까지 고려했을 때 운송할 수 있는 최대 손님 수
    dp = [[0] * (N + 1) for _ in range(4)]

    for i in range(1, 4):
        for j in range(i * trainLimit, N + 1):
            passengers = prefixSum[j] - prefixSum[j - trainLimit]
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-trainLimit] + passengers)

    return dp[3][N]

print(maxPassengers(N, train, trainLimit))