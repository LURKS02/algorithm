def count_paths(board, N):
    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            if dp[i][j] != 0 and board[i][j] != 0:
                jump = board[i][j]

                if j + jump < N:
                    dp[i][j + jump] += dp[i][j]

                if i + jump < N:
                    dp[i + jump][j] += dp[i][j]

    return dp[N-1][N-1]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

print(count_paths(board, N))