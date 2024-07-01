from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)

for _ in range(M):
    inputList = list(map(int, input().rstrip().split()))

    for i in range(1, len(inputList)-1):
        graph[inputList[i]].append(inputList[i+1])
        degree[inputList[i+1]] += 1

deq = deque()

result = []

for i in range(1, N+1):
    if degree[i] == 0:
        deq.append(i)

while deq:
    node = deq.popleft()
    result.append(node)

    for neighbor in graph[node]:
        degree[neighbor] -= 1
        if degree[neighbor] == 0:
            deq.append(neighbor)

if len(result) != N:
    print(0)
else:
    for r in result:
        print(r)
