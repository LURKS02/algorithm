N = int(input())
A = list(map(int, input().split()))

dp = [0 for _ in range(N)]

for i in range(len(A) - 1, -1, -1):
    if i == len(A) - 1:
        dp[i] = A[i]
    else:
        dp[i] = max((A[i] + dp[k] for k in range(i+1, len(A)) if A[i] < A[k]), default=A[i])

print(max(dp))