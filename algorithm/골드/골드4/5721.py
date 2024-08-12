while True:
    M, N = map(int, input().split())

    if M == 0 and N == 0: break

    box = [list(map(int, input().split())) for _ in range(M)]

    memory = [0] * (M)

    for i in range(M):
        tempDP = [[0] * 2 for _ in range(N)]
        tempDP[0][0] = 0
        tempDP[0][1] = box[i][0]

        for j in range(1, N):
            tempDP[j][0] = max(tempDP[j-1][0], tempDP[j-1][1])
            tempDP[j][1] = tempDP[j-1][0] + box[i][j]

        memory[i] = max(tempDP[N-1][0], tempDP[N-1][1])

    dp = [[0] * 2 for _ in range(M)]

    dp[0][0] = 0
    dp[0][1] = memory[0]

    if M == 1:
        print(memory[0])
        continue

    for i in range(1, M):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        dp[i][1] = dp[i-1][0] + memory[i]

    print(max(dp[M-1]))