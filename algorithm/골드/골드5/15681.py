import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
from collections import defaultdict
from collections import deque
N, R, Q = map(int, input().rstrip().split())

linkedDict = defaultdict(list)

for _ in range(N-1):
    U, V = map(int, input().rstrip().split())
    linkedDict[U].append(V)
    linkedDict[V].append(U)

parentDict = defaultdict(int)
childDict = defaultdict(list)

visited = [False] * (N+1)
deq = deque()
deq.append(R)
visited[R] = True

while deq:
    node = deq.popleft()
    for nextNode in linkedDict[node]:
        if not visited[nextNode]:
            visited[nextNode] = True
            parentDict[nextNode] = node
            childDict[node].append(nextNode)
            deq.append(nextNode)

size = [0] * (N+1)
def countSubtreeNodes(node):
    size[node] = 1
    for nextNode in childDict[node]:
        countSubtreeNodes(nextNode)
        size[node] += size[nextNode]

countSubtreeNodes(R)

# print(size)

for _ in range(Q):
    U = int(input().rstrip())
    print(size[U])