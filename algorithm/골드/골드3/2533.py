from collections import defaultdict
import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**9)

def dfs(node, parent):
    not_early = 0
    early = 1

    for child in tree[node]:
        if child != parent:
            child_not_early, child_early = dfs(child, node)
            not_early += child_early
            early += min(child_not_early, child_early)

    return not_early, early

N = int(input().rstrip())
tree = defaultdict(list)

for _ in range(N-1):
    u, v = map(int, input().rstrip().split())
    tree[u].append(v)
    tree[v].append(u)

not_early, early = dfs(1, 0)

print(min(not_early, early))

