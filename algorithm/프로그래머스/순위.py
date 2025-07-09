from collections import defaultdict, deque

def solution(n, results):
    winGraph = [[] for _ in range(n+1)]
    loseGraph = [[] for _ in range(n+1)]

    for result in results:
        winGraph[result[0]].append(result[1])
        loseGraph[result[1]].append(result[0])

    winDict = defaultdict(int)
    loseDict = defaultdict(int)

    for i in range(1, n+1):
        winDict[i] = count(i, winGraph)
        loseDict[i] = count(i, loseGraph)

    answer = 0
    for i in range(1, n+1):
        if winDict[i] + loseDict[i] == n-1:
            answer += 1
    return answer

def count(n, graph):
    visited = set()

    deq = deque([n])

    while deq:
        node = deq.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                deq.append(neighbor)

    return len(visited)

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))