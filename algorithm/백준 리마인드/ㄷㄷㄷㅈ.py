from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)
edges = []

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    edges.append((a, b))

dCount = 0
gCount = 0

for key in graph.keys():
    degree = len(graph[key])
    if degree >= 3:
        gCount += (degree * (degree-1) * (degree-2)) / 6

for edge in edges:
    ea, eb = edge
    dCount += (len(graph[ea])-1) * (len(graph[eb])-1)

if dCount > gCount * 3:
    print('D')
elif dCount < gCount * 3:
    print('G')
else:
    print('DUDUDUNGA')

