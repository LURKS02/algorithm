from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())

indegree = [0] * N
graph = [[] for _ in range(N)]
time = [0] * N

dp = [0] * N

for i in range(N):
    inputList = list(map(int, input().rstrip().split()))
    time[i] = inputList[0]
    ind = inputList[1]

    if ind != 0:
        for j in range(2, len(inputList)):
            graph[inputList[j] - 1].append(i)
            indegree[i] += 1

# print(graph)
q = deque()
for i in range(N):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = time[i]

# print(indegree)
# print(q)

while q:
    now = q.popleft()
    for next_task in graph[now]:
        indegree[next_task] -= 1
        dp[next_task] = max(dp[next_task], dp[now] + time[next_task])
        if indegree[next_task] == 0:
            q.append(next_task)

print(max(dp))