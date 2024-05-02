import sys
import heapq
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N, D, C = map(int, input().rstrip().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(D):
        A, B, S = map(int, input().rstrip().split())
        graph[B].append((A, S))

    heap = []
    cost = [float('inf')] * (N+1)
    heap.append((0, C))
    cost[C] = 0

    while heap:
        val, node = heapq.heappop(heap)

        if cost[node] < val:
            continue

        for neighbor, c in graph[node]:
            newVal = val + c
            if newVal < cost[neighbor]:
                cost[neighbor] = newVal
                heapq.heappush(heap, (newVal, neighbor))

    computers = 0
    time = 0

    for c in cost:
        if c != float('inf'):
            computers += 1
            time = max(time, c)

    print(computers, time)