N, C = map(int, input().split())

houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()

start = 0
end = houses[-1] - houses[0]
answer = end
while start <= end:
    mid = (start + end) // 2

    installedIndex = 0
    totalCount = 1

    for i in range(1, len(houses)):
        if houses[i] - houses[installedIndex] >= mid:
            installedIndex = i
            totalCount += 1

    if totalCount >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
