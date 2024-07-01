import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    want = int(input())

    dp = [0 for _ in range(want+1)]

    dp[0] = 1

    for i in range(N):
        for j in range(coins[i], want+1):
            dp[j] += dp[j-coins[i]]

    print(dp[want])