import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M = map(int, input().split())
names = [int(input()) for _ in range(N)]

maxNum = M * M * N
dp = [maxNum] * (N+1)
dp[N] = 0

def note(index: int):
    if dp[index] < maxNum:
        return dp[index]

    remain = M - names[index]

    for i in range(index+1, N+1):
        if remain >= 0:
            if i == N:
                dp[index] = 0
                break
            dp[index] = min(dp[index], remain*remain + note(i))
            remain -= names[i] + 1

    return dp[index]

print(note(0))


