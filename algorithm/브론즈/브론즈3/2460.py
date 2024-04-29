sum = 0
max = 0
for i in range(10):
    A, B = map(int, input().split())
    sum = sum - A + B
    if max < sum:
        max = sum


print(max)