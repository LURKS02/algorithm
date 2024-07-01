import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().rstrip().split())
    graph[A].append(B)
    degree[B] += 1

students = []
deq = deque()

for i in range(1, N+1):
    if degree[i] == 0:
        deq.append(i)

while deq:
    node = deq.popleft()
    students.append(node)

    for neighbor in graph[node]:
        degree[neighbor] -= 1
        if degree[neighbor] == 0:
            deq.append(neighbor)

print(*students)
