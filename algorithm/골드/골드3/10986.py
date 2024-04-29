N, M = map(int, input().split())
nums = list(map(int, input().split()))

prefix_count = [0] * M
prefix_count[0] = 1

prefix_sum = 0
result = 0

for num in nums:
    prefix_sum += num
    mod_value = prefix_sum % M

    result += prefix_count[mod_value]

    prefix_count[mod_value] += 1

print(result)