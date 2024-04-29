import heapq
import sys

input = sys.stdin.readline
INF = float('inf')

def dijkstra(start, N, graph):
    dist = [INF] * (N+1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if current_dist > dist[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return dist

def solve():
    N, E = map(int, input().rstrip().split())

    graph = [[] for _ in range(N+1)]

    for _ in range(E):
        a, b, c = map(int, input().rstrip().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    v1, v2 = map(int, input().rstrip().split())

    dist_from_1 = dijkstra(1, N, graph)
    dist_from_v1 = dijkstra(v1, N, graph)
    dist_from_v2 = dijkstra(v2, N, graph)

    path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]
    path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

    min_path = min(path1, path2)
    if min_path >= INF:
        print(-1)
    else:
        print(min_path)

solve()