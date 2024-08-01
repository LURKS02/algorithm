from collections import deque

N, M = map(int, input().split())
K = N // 2

heavyGraph = [[] for _ in range(N+1)]
lightGraph = [[] for _ in range(N+1)]

for _ in range(M):
    heavy, light = map(int, input().split())
    heavyGraph[light].append(heavy)
    lightGraph[heavy].append(light)

def checkHeavy(start):
    heavyCount = 0
    deq = deque()
    deq.append(start)
    visited = [False] * (N+1)
    visited[start] = True

    while deq:
        node = deq.popleft()

        for neighbor in heavyGraph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                heavyCount += 1
                deq.append(neighbor)

    return heavyCount

def checkLight(start):
    lightCount = 0
    deq = deque()
    deq.append(start)
    visited = [False] * (N+1)
    visited[start] = True

    while deq:
        node = deq.popleft()

        for neighbor in lightGraph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                lightCount += 1
                deq.append(neighbor)

    return lightCount

ans = 0
for i in range(1, N+1):
    if checkHeavy(i) > K or checkLight(i) > K:
        ans += 1

print(ans)