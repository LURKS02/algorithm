t = int(input())

for _ in range(t):
    # n = 주어진 정수의 개수 (1,000,000)
    # k = 주어지는 정수 (-100,000,000 ~ 100,000,000)
    n, k = map(int, input().split())

    l = list(map(int, input().split()))
    l.sort()

    left = 0
    right = n-1
    minDiff = float('inf')
    count = 0

    while left < right:
        currentSum = l[left] + l[right]
        currentDiff = abs(currentSum - k)

        if currentDiff < minDiff:
            minDiff = currentDiff
            count = 1

        elif currentDiff == minDiff:
            count += 1

        if currentSum < k:
            left += 1
        else:
            right -= 1

    print(count)


