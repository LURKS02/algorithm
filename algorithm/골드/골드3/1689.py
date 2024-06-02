import sys
import heapq

input = sys.stdin.readline
n = int(input())

arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[0])

heap = []
heapq.heappush(heap, arr[0][1])

result = 1

for x in arr[1:]:
    while heap and heap[0] <= x[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, x[1])
    result = max(result, len(heap))

print(result)
