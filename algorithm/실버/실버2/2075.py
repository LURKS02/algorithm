import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())

heap = []
for _ in range(N):
    l = list(map(int, input().split()))
    for num in l:
        if len(heap) < N:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)

print(heap[0])