import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [1] * (N+1)
arr = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)

for i in range(1, N+1):
    for b in arr[i]:
        graph[b] = max(graph[b], graph[i]+1)
print(*graph[1:])