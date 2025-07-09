from collections import defaultdict, deque

T = int(input())

for _ in range(T):
    N = int(input())
    t = list(map(int, input().split()))
    M = int(input())

    graph = defaultdict(list)
    degree = defaultdict(int)

    for i in range(len(t)-1):
        for j in range(i+1, len(t)):
            graph[t[i]].append(t[j])
            degree[t[j]] += 1

    for _ in range(M):
        a, b = map(int, input().split())

        if a in graph[b]:
            graph[b].remove(a)
            graph[a].append(b)
            degree[a] -= 1
            degree[b] += 1

        else:
            graph[a].remove(b)
            graph[b].append(a)
            degree[b] -= 1
            degree[a] += 1

    deq = deque()

    for k in range(1, N+1):
        if degree[k] == 0:
            deq.append(k)

    answer = []
    while deq:
        temp = deq.popleft()
        answer.append(temp)
        for neighbor in graph[temp]:
            degree[neighbor] -= 1
            if degree[neighbor] == 0:
                deq.append(neighbor)

    if len(answer) < N:
        print("IMPOSSIBLE")
    else:
        print(*answer)