import sys
input = sys.stdin.readline

# d = 탈출 거리 (1,000,000,000)
# n = 돌섬의 총 수 (50,000)
# m = 제거할 수 있는 총 수 (50,000)
d, n, m = map(int, input().rstrip().split())

# 출발지로부터 각 돌섬까지의 거리
distance = sorted([int(input().rstrip()) for _ in range(n)])

left = 0
right = d
answer = 0

while left <= right:
    mid = (left + right) // 2

    removedStones = 0
    now = 0
    minDistance = d
    for dist in distance:
        if dist - now >= mid:
            minDistance = min(minDistance, dist - now)
            now = dist
        else:
            removedStones += 1

    minDistance = min(minDistance, d - now)

    if removedStones > m:
        right = mid - 1
    else:
        answer = max(answer, minDistance)
        left = mid + 1

print(answer)






