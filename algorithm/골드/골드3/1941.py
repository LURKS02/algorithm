from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

graph = []
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
positions = [(i, j) for i in range(5) for j in range(5)]
combs = list(combinations(positions, 7))
answer = 0

for _ in range(5):
    graph.append(list(input().strip()))

def checkDasom(comb):
    dasom = 0
    for x, y in comb:
        if graph[x][y] == 'S':
            dasom += 1
    return True if dasom >= 4 else False

def checkAdjacent(comb):
    visited = [False] * 7
    deq = deque()
    deq.append(comb[0])
    visited[0] = True

    while deq:
        x, y = deq.popleft()
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]

            if (nx, ny) in comb:
                nextIdx = comb.index((nx, ny))
                if not visited[nextIdx]:
                    deq.append((nx, ny))
                    visited[nextIdx] = True

    return False if False in visited else True

for comb in combs:
    if checkDasom(comb):
        if checkAdjacent(comb):
            answer += 1

print(answer)