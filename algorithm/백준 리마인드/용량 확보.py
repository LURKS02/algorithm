import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, e = map(int, input().split())
    S = list(map(int, input().split()))
    doubleS = [k * 2 for k in S]

    totalPossible = sum(doubleS)
    if totalPossible < e:
        print("FULL")
    else:
        dp = [float('inf')] * (totalPossible + 1)
        dp[0] = 0

        for i in range(n):
            value = doubleS[i]
            weight = S[i]

            for v in range(totalPossible, value - 1, -1):
                dp[v] = min(dp[v], dp[v - value] + weight)

        answer = min(dp[e:])
        print(answer)

