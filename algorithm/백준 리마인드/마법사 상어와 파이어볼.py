import math
from collections import defaultdict

N, M, K = map(int, input().split())

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

graph = defaultdict(list)

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    graph[(r, c)].append((m, s, d))

for _ in range(K):
    keys = list(graph.keys())
    newGraph = defaultdict(list)
    for key in keys:
        while graph[key]:
            m, s, d = graph[key].pop()

            newR = (key[0] + dx[d] * s - 1) % N + 1
            newC = (key[1] + dy[d] * s - 1) % N + 1

            newGraph[(newR, newC)].append((m, s, d))

    graph = newGraph

    newGraph = defaultdict(list)
    keys = list(graph.keys())
    for key in keys:
        if len(graph[key]) >= 2:
            totalLen = len(graph[key])
            totalM = 0
            totalS = 0
            oddD = 0
            evenD = 0

            while graph[key]:
                m, s, d = graph[key].pop()
                totalM += m
                totalS += s

                if d % 2 == 0:
                    evenD += 1
                else:
                    oddD += 1

            newM = math.floor(totalM / 5)
            newS = math.floor(totalS / totalLen)
            if newM > 0 and (oddD == totalLen or evenD == totalLen):
                newGraph[key].append((newM, newS, 0))
                newGraph[key].append((newM, newS, 2))
                newGraph[key].append((newM, newS, 4))
                newGraph[key].append((newM, newS, 6))
            elif newM > 0:
                newGraph[key].append((newM, newS, 1))
                newGraph[key].append((newM, newS, 3))
                newGraph[key].append((newM, newS, 5))
                newGraph[key].append((newM, newS, 7))
        else:
            newGraph[key] = graph[key]

    graph = newGraph

totalM = 0

for key in graph.keys():
    for m, s, d in graph[key]:
        totalM += m

print(totalM)