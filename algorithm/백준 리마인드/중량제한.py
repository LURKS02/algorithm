from collections import defaultdict, deque

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

F, T = map(int, input().split())

left = 1
right = 1000000000

answer = 1

def canBFS(c):
    visited = [False] * (N + 1)
    deq = deque([F])
    visited[F] = True

    while deq:
        node = deq.popleft()

        if node == T:
            return True

        for neighbor, cost in graph[node]:
            if not visited[neighbor] and cost >= c:
                visited[neighbor] = True
                deq.append(neighbor)

    return False

while left <= right:
    mid = (left + right) // 2

    if canBFS(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)