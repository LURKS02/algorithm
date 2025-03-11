import heapq

N = int(input())
b = list(map(int, input().split()))

b.sort(key=lambda x: -x)

heap = []

time = 0
ans = 0
for num in b:
    heapq.heappush(heap, time + num)
    while heap[0] == time:
        heapq.heappop(heap)
    ans = max(ans, len(heap))
    time += 1

print(ans)
