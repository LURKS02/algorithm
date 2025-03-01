N = int(input())
A = list(map(int, input().split()))
Q = int(input())
L = list(map(int, input().split()))

sortedL = sorted(L)
maxLength = sortedL[-1]

dp = [0] * 100001

for stick in A:
    dp[stick] = 1

for i in range(1, 100001):
    if dp[i] == 0: continue
    for j in range(2 * i, 100001, i):
        dp[j] += dp[i]

# 결과 출력
answer = [dp[l] for l in L]
print(*answer)