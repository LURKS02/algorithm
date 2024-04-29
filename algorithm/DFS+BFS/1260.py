import sys
from collections import deque

input = sys.stdin.readline().split()
N, M, start = map(int, input)

graph = {i: [] for i in range(1, N + 1)}

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort()

dfsVisited = (N + 1) * [False]
bfsVisited = (N + 1) * [False]

def dfs(graph, v, dfsVisited):
    dfsVisited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if dfsVisited[i] == False:
            dfs(graph, i, dfsVisited)

dfs(graph, start, dfsVisited)

print()

def bfs(graph, start, bfsVisited):
    d = deque([start])
    bfsVisited[start] = True
    while d:
        num = d.popleft()
        print(num, end=' ')
        for i in graph[num]:
            if bfsVisited[i] == False:
                d.append(i)
                bfsVisited[i] = True

bfs(graph, start, bfsVisited)
