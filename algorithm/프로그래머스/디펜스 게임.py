import heapq

def solution(n, k, enemy):
    heap = []
    for (i, e) in enumerate(enemy):
        heapq.heappush(heap, e)
        if len(heap) > k:
            n -= heapq.heappop(heap)
        if n < 0:
            return i

    return len(enemy)