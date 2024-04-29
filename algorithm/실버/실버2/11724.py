import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)

N, M = map(int, sys.stdin.readline().rstrip().split())

g = defaultdict(list)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    g[u].append(v)
    g[v].append(u)

count = 0

visited = set()

def dfs(i):
    visited.add(i)
    for gr in g[i]:
        if gr not in visited:
            dfs(gr)

for k in g.keys():
    if k not in visited:
        dfs(k)
        count += 1

for i in range(1, N + 1):
    if i not in visited:
        count += 1
print(count)