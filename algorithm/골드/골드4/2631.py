import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = []

for _ in range(N):
    nums.append(int(input().rstrip()))

def length_of_lis(nums):
    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

print(N - length_of_lis(nums))