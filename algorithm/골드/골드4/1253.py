N = int(input())
nums = list(map(int, input().split()))

nums.sort()
numLength = len(nums)
goodCount = 0

for i in range(numLength):
    left, right = 0, numLength - 1

    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        current_sum = nums[left] + nums[right]

        if current_sum == nums[i]:
            goodCount += 1
            break
        elif current_sum < nums[i]:
            left += 1
        else:
            right -= 1

print(goodCount)





