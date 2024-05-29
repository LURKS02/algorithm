from collections import deque

person = int(input())

graph = [[] for _ in range(person)]

while True:
    A, B = map(int, input().split())
    if A == -1 and B == -1: break
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)


def bfs(start):
    deq = deque()
    deq.append(start)
    visited = [-1] * person
    visited[start] = 0

    while deq:
        node = deq.popleft()

        for neighbor in graph[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[node] + 1
                deq.append(neighbor)

    return max(visited)

answerMinValue = float('inf')
answerList = []

for i in range(person):
    maxValue = bfs(i)
    if maxValue < answerMinValue:
        answerMinValue = maxValue
        answerList = [i+1]
    elif maxValue == answerMinValue:
        answerList.append(i+1)

print(answerMinValue, len(answerList))
print(*answerList)
