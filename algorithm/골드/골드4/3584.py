from collections import deque
import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())

    graph = [[] for _ in range(N+1)]

    for _ in range(N-1):
        A, B = map(int, input().rstrip().split())
        graph[B].append(A)

    node1, node2 = map(int, input().rstrip().split())

    def getBestMatch(list1, list2):
        for num1 in list1:
            for num2 in list2:
                if num1 == num2:
                    return num1

    def bfs(start):
        deq = deque()
        deq.append(start)
        visited = [False] * (N+1)
        visited[start] = True
        parents = [start]

        while deq:
            node = deq.popleft()

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parents.append(neighbor)
                    deq.append(neighbor)

        return parents

    bfs1 = bfs(node1)
    bfs2 = bfs(node2)

    print(getBestMatch(bfs1, bfs2))
