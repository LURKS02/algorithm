import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

answer = []
graph = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]

heap = []

for i in range(M):
    A, B = map(int, input().rstrip().split())
    graph[A].append(B)
    degree[B] += 1

for i in range(1, N+1):
    if degree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    num = heapq.heappop(heap)
    answer.append(num)
    for i in graph[num]:
        degree[i] -= 1
        if degree[i] == 0:
            heapq.heappush(heap, i)

print(" ".join(map(str, answer)))