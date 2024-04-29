N = int(input())

nums = list(map(int, input().split()))

dp = [1] * N
path = [-1] * N

for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            path[i] = j

lis_length = max(dp)
lis_end = dp.index(lis_length)

lis = []
while lis_end != -1:
    lis.append(nums[lis_end])
    lis_end = path[lis_end]

lis.reverse()

print(lis_length)
print(*lis)