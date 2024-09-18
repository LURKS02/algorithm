import sys
input = sys.stdin.readline

Q = int(input().rstrip())

for _ in range(Q):
    a, d, x = map(int, input().split())

    left = 1
    right = 10**6

    floor, spot = -1, -1

    while left <= right:
        mid = (left + right) // 2
        # print(left, right)
        # print(mid)
        firstInMid = (mid-1)*a + ((mid-1) * (mid-2) // 2) * d + 1

        if x >= firstInMid:
            left = mid + 1
            floor = mid
        else:
            right = mid - 1

    spot = x - ((floor-1)*a + ((floor-1) * (floor-2) // 2) * d + 1) + 1

    print(floor, spot)