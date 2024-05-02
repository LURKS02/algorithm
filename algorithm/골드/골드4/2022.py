import sys
import math
input = sys.stdin.readline

x, y, c = map(float, input().split())

left, right = 0, min(x, y)
result = 0

while right - left > 1e-6:
    mid = (right + left) / 2.0
    h1 = math.sqrt(x**2 - mid**2)
    h2 = math.sqrt(y**2 - mid**2)

    cross_height = (h1 * h2) / (h1 + h2)

    if cross_height < c:
        right = mid
    else:
        left = mid
        result = mid

print(f"{result:.3f}")