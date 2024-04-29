import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

M, N, L = map(int, input().rstrip().split())
guns = sorted(list(map(int, input().rstrip().split())))
animals = [tuple(map(int, input().rstrip().split())) for _ in range(N)]

def countCatchable():
    catchable = 0

    for x, y in animals:
        idx = bisect_left(guns, x)

        if idx > 0 and abs(guns[idx-1] - x) + y <= L:
            catchable += 1
        elif idx < M and abs(guns[idx] - x) + y <= L:
            catchable += 1

    return catchable

print(countCatchable())
