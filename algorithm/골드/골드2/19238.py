import math
from collections import deque

n, m, energy = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
startX, startY = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    visited = [[-1] * n for _ in range(n)]
    deq = deque()
    deq.append((x, y))
    visited[x][y] = 0

    while deq:
        curX, curY = deq.popleft()

        for i in range(4):
            nx, ny = curX + dx[i], curY + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[curX][curY] + 1
                deq.append((nx, ny))

    return visited

def checkDist(visited: list, people: list):
    i = 0

    for px, py, ax, ay in people:
        people[i].append(visited[px-1][py-1])
        i += 1

    people.sort(key=lambda x: (-x[4], -x[0], -x[1]))

def solve(x, y):
    global energy
    while people:
        visited = bfs(x-1, y-1)
        checkDist(visited, people)
        px, py, ax, ay, dist = people.pop()

        for temp in people:
            temp.pop()

        visited = bfs(px-1, py-1)
        dist2 = visited[ax-1][ay-1]
        x, y = ax, ay

        if dist == -1 or dist2 == -1:
            print(-1)
            return

        energy -= dist
        if energy < 0:
            break
        energy -= dist2
        if energy < 0:
            break

        energy += dist2 * 2

    if energy < 0:
        print(-1)
    else:
        print(energy)

solve(startX, startY)