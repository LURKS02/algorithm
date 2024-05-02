import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

case = int(input().rstrip())

for _ in range(case):
    N, M, T = map(int, input().rstrip().split())
    S, G, H = map(int, input().rstrip().split())

    graph = [[] for _ in range(N+1)]
    picks = []
    dist = -1

    for _ in range(M):
        A, B, D = map(int, input().rstrip().split())
        graph[A].append((B, D))
        graph[B].append((A, D))
        if (A == G and B == H) or (B == G and A == H):
            dist = D

    for _ in range(T):
        picks.append(int(input().rstrip()))

    # G에서 출발
    Gcost = [INF] * (N+1)
    heap = []
    Gcost[G] = 0
    heap.append((0, G))

    while heap:
        val, node = heapq.heappop(heap)

        if Gcost[node] < val:
            continue

        for neighbor, value in graph[node]:
            newValue = val + value
            if Gcost[neighbor] > newValue:
                Gcost[neighbor] = newValue
                heapq.heappush(heap, (newValue, neighbor))


    # H에서 출발
    Hcost = [INF] * (N + 1)
    heap = []
    Hcost[H] = 0
    heap.append((0, H))

    while heap:
        val, node = heapq.heappop(heap)

        if Hcost[node] < val:
            continue

        for neighbor, value in graph[node]:
            newValue = val + value
            if Hcost[neighbor] > newValue:
                Hcost[neighbor] = newValue
                heapq.heappush(heap, (newValue, neighbor))

    startToG = Gcost[S]
    startToH = Hcost[S]

    startCost = [INF] * (N + 1)
    heap = []
    startCost[S] = 0
    heap.append((0, S))

    while heap:
        val, node = heapq.heappop(heap)

        if startCost[node] < val:
            continue

        for neighbor, value in graph[node]:
            newValue = val + value
            if startCost[neighbor] > newValue:
                startCost[neighbor] = newValue
                heapq.heappush(heap, (newValue, neighbor))

    ans = []

    for pick in picks:
        distance = min(startToG + Hcost[pick], startToH + Gcost[pick]) + dist
        if startCost[pick] >= distance:
            ans.append(pick)

    print(*sorted(ans))