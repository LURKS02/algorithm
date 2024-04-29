import sys
input = sys.stdin.readline

N, C = map(int, input().rstrip().split())
houses = [int(input().rstrip()) for _ in range(N)]

houses.sort()

def can_place_routers(houses, distance, C):
    count = 1
    last_placed = houses[0]

    for i in range(1, len(houses)):
        if houses[i] - last_placed >= distance:
            count += 1
            last_placed = houses[i]
            if count >= C:
                return True

    return False

low = 1
high = houses[-1] - houses[0]
result = 0

while low <= high:
    mid = (low + high) // 2
    if can_place_routers(houses, mid, C):
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)