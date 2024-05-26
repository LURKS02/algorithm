import sys
input = sys.stdin.readline

# N = 날짜 수 (1,500,000)
N = int(input().rstrip())

times = []
pays = []

for _ in range(N):
    # T = 상담 기간 (50)
    # P = 받을 수 있는 금액 (1,000)
    T, P = map(int, input().rstrip().split())
    times.append(T)
    pays.append(P)

dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i-1])
    finDate = i + times[i-1] - 1
    if finDate <= N:
        dp[finDate] = max(dp[finDate], dp[i-1] + pays[i-1])

print(max(dp))