from collections import deque

V, E, P = map(int, input().split())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

canCost = [float('inf')] * (V+1)
cannotCost = [float('inf')] * (V+1)

deq = deque()
visited = [False] * (V+1)
visited[1] = True

deq.append((1, 0, False))

while deq:
    node, c, vst = deq.popleft()

    if node == P:
        vst = True

    for (neighbor, value) in graph[node]:
        newValue = c + value
        if vst:
            if newValue < canCost[neighbor]:
                canCost[neighbor] = newValue
                deq.append((neighbor, newValue, vst))
        else:
            if newValue < cannotCost[neighbor]:
                cannotCost[neighbor] = min(cannotCost[neighbor], newValue)
                deq.append((neighbor, newValue, vst))

# print(canCost)
# print(cannotCost)

if canCost[V] <= cannotCost[V]:
    print("SAVE HIM")

else:
    print("GOOD BYE")