import sys
from collections import defaultdict

def check(start):
    ret = True
    deq = [start]

    while deq:
        node = deq.pop()
        if visited[node] == True:
            ret =  False
        visited[node] = True
        for nextNode in dict[node]:
            if nextNode == node:
                ret =  False
            if visited[nextNode] == False:
                deq.append(nextNode)

    return ret

cnt = 0

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    ans = 0
    cnt += 1
    dict = defaultdict(list)
    visited = [False] * (n+1)

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        dict[a].append(b)
        dict[b].append(a)

    for i in range(1, n+1):
        if not visited[i] and check(i):
            ans += 1

    if ans > 1:
        print("Case %d: A forest of %d trees." % (cnt,ans))
    elif ans == 1:
        print("Case %d: There is one tree." % cnt)
    else:
        print("Case %d: No trees." % cnt)