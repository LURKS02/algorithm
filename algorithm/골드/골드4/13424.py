import heapq
# T = 테스트 케이스의 개수
T = int(input())

for _ in range(T):
    # N = 방의 개수 (100)
    # M = 비밀통로의 개수 (99~4950)
    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    # K = 모임에 참여하는 친구의 수 (100)
    K = int(input())

    # rooms = 친구들이 위치하는 방 번호
    rooms = list(map(int, input().split()))
    ansNumber = -1
    ansValue = float('inf')

    for i in range(1, N+1):
        heap = []
        cost = [float('inf')] * (N+1)
        heap.append((0, i))
        cost[i] = 0

        while heap:
            c, node = heapq.heappop(heap)

            if c > cost[node]:
                continue

            for neighbor, value in graph[node]:
                newValue = c + value
                if newValue < cost[neighbor]:
                    cost[neighbor] = newValue
                    heapq.heappush(heap, (newValue, neighbor))

        caseSum = sum([cost[r] for r in rooms])
        if caseSum < ansValue:
            ansValue = caseSum
            ansNumber = i

    print(ansNumber)