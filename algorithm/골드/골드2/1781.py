import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())
assignments = []

for _ in range(N):
    d, c = map(int, input().rstrip().split())
    assignments.append((d, c))

assignments.sort(key=lambda x: x[0])

minHeap = []

for deadline, cups in assignments:
    heapq.heappush(minHeap, cups)
    if len(minHeap) > deadline:
        heapq.heappop(minHeap)

max_cups = sum(minHeap)
print(max_cups)