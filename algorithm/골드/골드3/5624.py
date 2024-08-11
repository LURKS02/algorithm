N = int(input())
nums = list(map(int, input().split()))

sets = set()
sets.add(nums[0] + nums[0])

count = 0

for i in range(1, N):
    for j in range(i):
        if nums[i] - nums[j] in sets:
            count += 1
            break

    for j in range(i+1):
        sets.add(nums[i] + nums[j])

print(count)