from collections import deque

N = int(input())
l = []
for i in range(N):
    l.append(list(map(int, input().split())))

in_degree = [0] * (N + 1)
build_time = [0] * (N + 1)
max_time = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    info = l[i-1]
    build_time[i] = info[0]

    for pre in info[1:]:
        if pre == -1:
            break
        graph[pre].append(i)
        in_degree[i] += 1

queue = deque()

for i in range(1, N + 1):
    if in_degree[i] == 0:
        queue.append(i)
        max_time[i] = build_time[i]

while(queue):
    now = queue.popleft()
    for next_node in graph[now]:
        in_degree[next_node] -= 1
        max_time[next_node] = max(max_time[next_node], max_time[now] + build_time[next_node])
        if in_degree[next_node] == 0:
            queue.append(next_node)

for i in range(1, len(max_time)):
    print(max_time[i])