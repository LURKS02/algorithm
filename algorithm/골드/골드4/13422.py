import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N, M, K = map(int, input().rstrip().split())
    houses = list(map(int, input().rstrip().split()))

    cycleHouses = houses + houses[:-1]

    if N == M:
        s = sum(houses)
        if s < K:
            print(1)
            continue
        else:
            print(0)
            continue

    start = 0
    end = 0
    currentSum = cycleHouses[0]
    currentCount = 1

    ans = 0

    while start < N and end < len(cycleHouses):
        if currentCount < M:
            end += 1
            currentSum += cycleHouses[end]
            currentCount += 1
        elif currentCount > M:
            currentSum -= cycleHouses[start]
            start += 1
            currentCount -= 1
        else:
            if currentSum < K:
                ans += 1

                end += 1
                currentSum += cycleHouses[end]
                currentCount += 1

            else:
                currentSum -= cycleHouses[start]
                start += 1
                currentCount -= 1

    print(ans)
