import sys
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)

def findCycle(N, graph):
    parent = [-1] * (N+1)
    visited = [False] * (N+1)
    cycle = []

    def dfs(v):
        visited[v] = True
        for next in graph[v]:
            if not visited[next]:
                parent[next] = v
                if dfs(next):
                    return True

            elif visited[next] and parent[v] != next:
                cycleNode = v
                cycle.append(cycleNode)
                while cycleNode != next:
                    cycleNode = parent[cycleNode]
                    cycle.append(cycleNode)
                cycle.append(next)
                return True

        return False

    for i in range(1, N+1):
        if not visited[i]:
            if dfs(i):
                break

    return cycle

def calculateDistances(N, graph, cycle):
    distances = [-1] * (N+1)
    queue = deque(cycle)
    for node in cycle:
        distances[node] = 0

    while queue:
        current = queue.popleft()
        currentDist = distances[current]
        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = currentDist + 1
                queue.append(neighbor)

    return distances[1:]

N = int(input())
graph = defaultdict(list)
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cycle = findCycle(N, graph)
distances = calculateDistances(N, graph, cycle)

print(' '.join(map(str, distances)))