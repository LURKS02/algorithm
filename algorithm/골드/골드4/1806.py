N, S = map(int, input().split())
numbers = list(map(int, input().split()))

start, end = 0, 0

currentSum = 0
min_length = N + 1

while True:
    if currentSum >= S:
        min_length = min(min_length, end - start)
        currentSum -= numbers[start]
        start += 1
    elif end == N:
        break
    else:
        currentSum += numbers[end]
        end += 1

if min_length <= N:
    print(min_length)
else:
    print(0)