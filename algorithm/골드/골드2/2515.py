import sys
input = sys.stdin.readline

N, S = map(int, input().rstrip().split())
paintings = dict()
maxHeight = 0

for _ in range(N):
    H, C = map(int, input().rstrip().split())
    maxHeight = max(maxHeight, H)

    if H in paintings:
        paintings[H] = max(paintings[H], C)
    else:
        paintings[H] = C

heights = [0] * (maxHeight + 1)

for h in range(1, len(heights)):
    if h in paintings:
        newCost = paintings[h]
        if h >= S:
            newCost += heights[h-S]
        heights[h] = max(heights[h-1], newCost)
    else:
        heights[h] = heights[h-1]

print(heights[-1])