import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

graph = defaultdict(list)

N = int(input())

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[-1, -1] for _ in range(N+1)]

def dfs(node, pre, flag):
    if dp[node][flag] != -1:
        return dp[node][flag]

    dp[node][flag] = flag

    for next in graph[node]:
        if next == pre:
            continue
        if flag:
            dp[node][flag] += min(dfs(next, node, 0), dfs(next, node, 1))
        else:
            dp[node][flag] += dfs(next, node, 1)

    return dp[node][flag]

result = min(dfs(1, 0, 0), dfs(1, 0, 1))
print(result)