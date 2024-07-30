import sys
import heapq
from collections import deque

N, M = map(int, input().rstrip().split())
students = [deque(sorted(list(map(int, input().split())))) for _ in range(N)]

heap = []

maxValue = 0
minValue = float('inf')

for i in range(len(students)):
    val = students[i].popleft()
    maxValue = max(maxValue, val)
    minValue = min(minValue, val)
    heapq.heappush(heap, (val, i))

answer = maxValue - minValue
# print(heap)
while heap:
    prevMinValue, pos = heapq.heappop(heap)
    if not students[pos]:
        break
    newValue = students[pos].popleft()
    heapq.heappush(heap, (newValue, pos))

    if maxValue < newValue:
        maxValue = newValue
    minValue = heap[0][0]
    answer = min(answer, maxValue - minValue)

print(answer)