import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
seats = []
idx = 0

schedules = []

for _ in range(N):
    P, Q = map(int, input().split())
    schedules.append((P, Q))

schedules.sort()

count = [0 for _ in range(100000)]

maxValue = 0

for startTime, endTime in schedules:
    if len(heap) == 0:
        heap.append((endTime, idx))
        count[idx] += 1
        idx += 1
        maxValue = max(maxValue, len(heap))
        continue

    while len(heap) > 0 and heap[0][0] <= startTime:
        et, i = heapq.heappop(heap)
        heapq.heappush(seats, i)

    if len(seats) == 0:
        heapq.heappush(heap, (endTime, idx))
        count[idx] += 1
        idx += 1
        maxValue = max(maxValue, len(heap))
        continue

    i = heapq.heappop(seats)
    heapq.heappush(heap, (endTime, i))
    count[i] += 1


print(maxValue)
for i in range(maxValue):
    print(count[i], end=' ')
