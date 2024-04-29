N, M = map(int, input().split())

num = []

for _ in range(N):
    num.append(int(input()))

num.sort()

left = 0
right = 1

if len(num) > 1:
    minDiff = num[-1] - num[0]
else:
    minDiff = 0

while left < len(num) and right < len(num):
    # print(right, left)
    currentDiff = num[right] - num[left]

    if currentDiff >= M:
        minDiff = min(minDiff, currentDiff)
        left += 1
    else:
        right += 1

print(minDiff)