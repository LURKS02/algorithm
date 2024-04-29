N, M = map(int, input().split())

A = list(map(int, input().split()))

end = 0
count = 0

sum = 0

for start in range(N):
    while sum < M and end < N:
        sum += A[end]
        end += 1
    if sum == M:
        count += 1
    sum -= A[start]

print(count)