from collections import deque

# N = 물건의 개수
N = int(input())

# M = 측정된 물건 쌍의 개수
M = int(input())

heavyGraph = [[] for _ in range(N+1)]
lightGraph = [[] for _ in range(N+1)]

for _ in range(M):
    heavy, light = map(int, input().split())
    heavyGraph[light].append(heavy)
    lightGraph[heavy].append(light)

def heavyBfs(start):
    deq = deque()
    deq.append(start)
    visited = [False] * (N+1)
    visited[start] = True

    while deq:
        node = deq.popleft()

        for neighbor in heavyGraph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                deq.append(neighbor)

    return visited.count(True) - 1


def lightBfs(start):
    deq = deque()
    deq.append(start)
    visited = [False] * (N + 1)
    visited[start] = True

    while deq:
        node = deq.popleft()

        for neighbor in lightGraph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                deq.append(neighbor)

    return visited.count(True) - 1

for i in range(1, N+1):
    visitedCount = heavyBfs(i) + lightBfs(i) + 1
    print(N - visitedCount)
