import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def bfs(start, graph):
    visited = {}
    queue = deque([(start, 0)])
    farthestNode = start
    maxDistance = 0

    while queue:
        current, dist = queue.popleft()
        if current in visited:
            continue
        visited[current] = dist
        if dist > maxDistance:
            maxDistance = dist
            farthestNode = current

        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, dist + weight))

    return farthestNode, maxDistance

def findTreeDiameter(graph):
    farthestFromStart, _ = bfs(1, graph)
    _, diameter = bfs(farthestFromStart, graph)
    return diameter

V = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(V):
    data = list(map(int, input().split()))
    node = data[0]
    for i in range(1, len(data)-1, 2):
        graph[node].append((data[i], data[i+1]))

print(findTreeDiameter(graph))