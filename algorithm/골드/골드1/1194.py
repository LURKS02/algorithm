from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, grid, N, M):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    deq = deque([(start[0], start[1], 0, 0)])
    visited = set([(start[0], start[1], 0)])

    while deq:
        x, y, keys, steps = deq.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                cell = grid[nx][ny]

                if cell == '#':
                    continue

                if cell == '1':
                    return steps + 1

                new_keys = keys
                if 'a' <= cell <= 'f':
                    new_keys |= (1 << (ord(cell) - ord('a')))

                if 'A' <= cell <= 'F':
                    if not (keys & (1 << (ord(cell) - ord('A')))):
                        continue

                if (nx, ny, new_keys) not in visited:
                    visited.add((nx, ny, new_keys))
                    deq.append((nx, ny, new_keys, steps + 1))

    return -1

N, M = map(int, input().rstrip().split())
grid = []
start = None

for i in range(N):
    row = [s for s in input().rstrip()]
    grid.append(row)
    if '0' in row:
        start = (i, row.index('0'))

print(bfs(start, grid, N, M))
