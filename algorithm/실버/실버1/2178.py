from collections import deque

N, M = map(int, input().split())
l = []

for _ in range(N):
    new = input()
    l.append([int(k) for k in new])

visited = [[False for _ in range(M)] for _ in range(N)]

def bfs(x, y):
    deq = deque()
    count = 1

    deq.append((x, y, count))

    while deq:

        current = deq.popleft()

        if current[0] < N and current[1] < M and current[0] >= 0 and current[1] >= 0  and not visited[current[0]][current[1]] and l[current[0]][current[1]] != 0:
            visited[current[0]][current[1]] = True

            if current[0] == N - 1 and current[1] == M - 1:
                print(current[2])
                break

            else:
                deq.append((current[0], current[1]-1, current[2] + 1))
                deq.append((current[0]-1, current[1], current[2] + 1))
                deq.append((current[0]+1, current[1], current[2] + 1))
                deq.append((current[0], current[1] + 1, current[2] + 1))

bfs(0, 0)