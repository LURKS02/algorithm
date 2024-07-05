import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
people = set(input().rstrip().split())

child = { person: [] for person in people }
edge = { person: [] for person in people }
indegree = { person: 0 for person in people }
father = []

M = int(input())
for _ in range(M):
    A, B = input().rstrip().split()
    indegree[A] += 1
    edge[B].append(A)

deq = deque()
for person in people:
    if indegree[person] == 0:
        deq.append(person)
        father.append(person)

while deq:
    node = deq.popleft()
    for next in edge[node]:
        indegree[next] -= 1
        if indegree[next] == 0:
            deq.append(next)
            child[node].append(next)

print(len(father))
print(*sorted(father))
for name in sorted(list(people)):
    printStr = name + " " + str(len(child[name]))
    if len(child[name]) != 0:
        printStr += (" " + " ".join(sorted(child[name])))
    print(printStr)