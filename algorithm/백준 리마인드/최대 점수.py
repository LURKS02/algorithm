import sys
input = sys.stdin.readline

N, K = map(int, input().split())
l = list(map(int, input().split()))

dp = [0 for _ in range(N+1)]

left = 0
right = 1
current = l[left]

while right <= N:
    if current >= K:
        while current >= K:
            dp[right] = max(dp[right], dp[left] + current - K)
            current -= l[left]
            left += 1
    else:
        dp[right] = max(dp[right], dp[right-1])

        if right == N:
            break

        current += l[right]
        right += 1

print(dp[N])