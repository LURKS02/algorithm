import math

T = int(input())

def getDistance(x1, y1, x2, y2):
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())

    n = int(input())
    count = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        d1 = getDistance(x1, y1, cx, cy)
        d2 = getDistance(x2, y2, cx, cy)

        if d1 <= r and d2 <= r:
            continue
        elif getDistance(x1, y1, cx, cy) <= r:
            count += 1
        elif getDistance(x2, y2, cx, cy) <= r:
            count += 1
    print(count)