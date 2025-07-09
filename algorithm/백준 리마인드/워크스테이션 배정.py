import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

timetable = []

for _ in range(N):
    a, s = map(int, input().split())
    timetable.append((a, s))

timetable.sort()

answer = 0
heap = []
for arriving, interval in timetable:
    if not heap:
        heap.append(arriving + interval)

    else:
        while heap and heap[0] + M < arriving:
            heapq.heappop(heap)
        if heap:
            if heap[0] <= arriving <= heap[0] + M:
                leaveTime = heapq.heappop(heap)
                answer += 1
                heapq.heappush(heap, arriving + interval)
            else:
                heapq.heappush(heap, arriving + interval)
        else:
            heapq.heappush(heap, arriving + interval)

print(answer)