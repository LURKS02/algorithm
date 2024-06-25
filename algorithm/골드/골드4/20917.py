T = int(input())
for _ in range(T):
    n, s = map(int, input().split())
    spots = sorted(list(map(int, input().split())))

    start, end = 1, 1000000000
    ans = -1
    while start <= end:
        mid = (start + end) // 2

        current = spots[0]
        chairs = 1
        for i in range(1, n):
            if spots[i] - current >= mid:
                chairs += 1
                current = spots[i]

        if chairs >= s:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

    print(ans)