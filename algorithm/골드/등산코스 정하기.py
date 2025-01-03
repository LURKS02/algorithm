import heapq

def solution(n, paths, gates, summits):
    summitSet = set(summits)
    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))

    heap = []
    MAX = 1e9
    distance = [MAX] * (n + 1)
    answerSummit = MAX
    answer = MAX

    for gate in gates:
        heapq.heappush(heap, (0, gate))
        distance[gate] = 0

    while heap:
        value, node = heapq.heappop(heap)
        if distance[node] < value:
            continue

        if node in summitSet:
            if answer >= value:
                answer = value
                answerSummit = min(answerSummit, node)
            continue

        for neighbor, cost in graph[node]:
            newMax = max(value, cost)
            if distance[neighbor] > newMax:
                heapq.heappush(heap, (newMax, neighbor))
                distance[neighbor] = newMax

    return [answerSummit, answer]

print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [2], [3, 4]))