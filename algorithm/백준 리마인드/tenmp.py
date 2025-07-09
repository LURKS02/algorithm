import heapq
from collections import defaultdict

def prim(graph, start_node):
    mst = list()
    edges = defaultdict(list)

    for n1, n2, weight in graph:
        edges[n1].append((weight, n1, n2))
        edges[n2].append((weight, n2, n1))

    connected = set([start_node])

    connectedEdgeList = edges[start_node]
    heapq.heapify(connectedEdgeList)

    while connectedEdgeList:
        weight, n1, n2 = heapq.heappop(connectedEdgeList)

        if n2 not in connected:
            connected.add(n2)
            mst.append((weight, n1, n2))

            for edge in edges[n2]:
                if edge[2] not in connected:
                    heapq.heappush(connectedEdgeList, edge)
    return mst

def solution(n, costs):
    answerList = prim(costs, 1)
    cnt = sum([answer[0] for answer in answerList])
    return cnt