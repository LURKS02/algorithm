import sys
from collections import deque
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

N, M, K, X = map(int, input().rstrip().split())

l = dict()

for _ in range(M):
    A, B = map(int, input().rstrip().split())
    if A in l:
        l[A].append(B)
    else:
        l[A] = [B]

city = set()
visited = [False for _ in range(N + 1)]

def visit(start, count):
    d = deque([(start, count)])
    visited[start] = True

    cnt = count
    while d:
        c = d.popleft()
        if c[1] == K:
            city.add(c[0])

        cnt = c[1] + 1
        if c[0] in l:
            for g in l[c[0]]:
                if not visited[g]:
                    d.append((g, cnt))
                    visited[g] = True

visit(X, 0)

if len(city) == 0:
    print(-1)
else:
    city = sorted(list(city))
    for n in city:
        print(n)