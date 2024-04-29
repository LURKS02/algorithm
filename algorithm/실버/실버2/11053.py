
N = int(input())

l = list(map(int, input().split()))

dp = [-1] * N

for i in range(len(l) - 1, -1, -1):
    if i == len(l) - 1:
        dp[-1] = 1
    else:
        values = [dp[x] + 1 for x in range(i + 1, len(l)) if l[x] > l[i]]
        dp[i] = max(values) if values else 1

print(max(dp))