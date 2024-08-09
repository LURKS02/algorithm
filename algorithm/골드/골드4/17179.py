N, M, L = map(int, input().split())
canCut = []

for _ in range(M):
    canCut.append(int(input()))
canCut.append(L)

minLength = float('inf')
index = 0
for cut in canCut:
    minLength = min(minLength, cut - index)
    index = cut

minLength = min(minLength, L - index)

# print(minLength)

for _ in range(N):
    Q = int(input())

    ans = minLength
    start = minLength
    end = 4000000

    while start <= end:
        mid = (start + end) // 2

        parseCount = 0
        currentIndex = 0

        for cut in canCut:
            length = cut - currentIndex
            if length >= mid:
                parseCount += 1
                currentIndex = cut

        # print(mid, parseCount)

        if parseCount > Q:
            start = mid + 1
            # ans = max(ans, mid)
            ans = mid
        else:
            end = mid - 1

    print(ans)