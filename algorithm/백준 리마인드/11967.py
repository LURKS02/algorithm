from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lights = defaultdict(list)

for _ in range(M):
    x, y, a, b = map(int, input().split())
    lights[(x, y)].append((a, b))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

lighted = set()
visited = set()

deq = deque()
deq.append((1, 1))
lighted.add((1, 1))
visited.add((1, 1))

while deq:
    x, y = deq.popleft()

    for lx, ly in lights[(x, y)]:
        if (lx, ly) not in lighted:
            lighted.add((lx, ly))
            for i in range(4):
                nx, ny = lx + dx[i], ly + dy[i]
                if (nx, ny) in visited:
                    deq.append((nx, ny))

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 1 <= nx <= N and 1 <= ny <= N and (nx, ny) not in visited:
            if (nx, ny) in lighted:
                deq.append((nx, ny))
                visited.add((nx, ny))

print(len(lighted))