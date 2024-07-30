from collections import deque, defaultdict

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    if N == 1:
        print(0)
        continue

    parentGraph = dict()
    childGraph = dict()

    graph = defaultdict(list)

    for i in range(1, N+1):
        parentGraph[i] = []
        childGraph[i] = []

    for _ in range(M):
        A, B, D = map(int, input().split())
        graph[A].append((B, D))
        graph[B].append((A, D))

    deq = deque([1])
    visited = [False] * (N+1)
    visited[1] = True

    while deq:
        node = deq.popleft()

        for neighbor, c in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parentGraph[neighbor].append((node, c))
                childGraph[node].append((neighbor, c))
                deq.append(neighbor)

    leafSet = set()
    for k in childGraph.keys():
        if len(childGraph[k]) == 0:
            leafSet.add(k)

    cost = [float('inf')] * (N+1)
    for leaf in leafSet:
        if leaf != 1:
            cost[leaf] = parentGraph[leaf][0][1]

    def getDP(node):
        if cost[node] != float('inf'):
            return cost[node]

        if len(childGraph[node]) == 0:
            cost[node] = parentGraph[node][0][1]
            return cost[node]

        sum = 0
        for neighbor, value in childGraph[node]:
            sum += getDP(neighbor)
        cost[node] = sum
        if node != 1:
            cost[node] = min(cost[node], parentGraph[node][0][1])
        return cost[node]

    print(getDP(1))