from collections import defaultdict
import heapq

N = int(input())

dict = defaultdict(list)
heap = []

for _ in range(N):
    deadline, cups = map(int, input().split())
    dict[deadline].append(cups)

time = N
totalCups = 0

while True:
    if time == 0:
        break
    for cup in dict[time]:
        heapq.heappush(heap, -cup)

    if heap:
        cups = heapq.heappop(heap)
        totalCups += cups
    time -= 1

print(-totalCups)