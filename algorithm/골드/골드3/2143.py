from collections import defaultdict

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

sum_count_A = defaultdict(int)

for start in range(n):
    current_sum = 0
    for end in range(start, n):
        current_sum += A[end]
        sum_count_A[current_sum] += 1

result_count = 0
for start in range(m):
    current_sum = 0
    for end in range(start, m):
        current_sum += B[end]
        complement = T - current_sum
        if complement in sum_count_A:
            result_count += sum_count_A[complement]

print(result_count)