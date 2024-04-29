import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N, M = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

start, end = map(int, input().split())

left = 1
right = 1000000000

def check(cur, weight):
    global end
    if cur == end:
        return True

    for node, bridgeW in graph[cur]:
        if bridgeW >= weight and not visited[node]:
            visited[node] = True
            if check(node, weight):
                return True

    return False

while left <= right:
    mid = (left + right) // 2
    visited = [False] * (N+1)
    visited[start] = True

    if check(start, mid):
        left = mid + 1
    else:
        right = mid - 1

print(right)