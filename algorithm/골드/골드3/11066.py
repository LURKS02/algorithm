T = int(input())

for _ in range(T):
    K = int(input())
    matrix = list(map(int, input().split()))

    dp = [[0] * (K + 1) for _ in range(K + 1)]
    prefix_sum = [0] * (K + 1)

    for i in range(1, K+1):
        prefix_sum[i] = prefix_sum[i-1] + matrix[i-1]

    for length in range(2, K + 1):
        for start in range(1, K - length + 2):
            end = start + length - 1
            dp[start][end] = float('inf')

            for mid in range(start, end):
                cost = dp[start][mid] + dp[mid+1][end] + prefix_sum[end] - prefix_sum[start - 1]
                dp[start][end] = min(dp[start][end], cost)

    print(dp[1][K])

