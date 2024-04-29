import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

jewels = []
for _ in range(N):
    M, V = map(int, input().rstrip().split())
    heapq.heappush(jewels, (M, V))

bags = []
for _ in range(K):
    C = int(input())
    heapq.heappush(bags, C)

availableJewels = []
value = 0

while bags:
    capacity = heapq.heappop(bags)
    while jewels and jewels[0][0] <= capacity:
        weight, val = heapq.heappop(jewels)
        heapq.heappush(availableJewels, -val)

    if availableJewels:
        value += -heapq.heappop(availableJewels)

print(value)


