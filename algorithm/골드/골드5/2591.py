nums = [int(c) for c in input()]

N = len(nums)

dp = [0] * (N+1)

dp[0] = 1
dp[1] = 1

for k in range(2, N+1):
    if nums[k-1] != 0:
        dp[k] = dp[k-1]

    num1 = nums[k-2]
    num2 = nums[k-1]
    if num1 != 0:
        totalNum = num1*10 + num2

        if totalNum <= 34 and totalNum >= 1:
            dp[k] += dp[k-2]

# print(dp)

print(dp[N])

