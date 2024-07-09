import sys
sys.setrecursionlimit(10**9)

N, P, Q = map(int, input().split())
dp = dict()

dp[0] = 1

def getDP(n):
    if n in dp:
        return dp[n]

    val = getDP(n//P) + getDP(n//Q)
    dp[n] = val
    return val

print(getDP(N))