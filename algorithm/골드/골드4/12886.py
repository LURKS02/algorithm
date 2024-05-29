from collections import deque

a, b, c = map(int, input().split())
visited = [[False] * 1501 for _ in range(1501)]

total = a + b + c

def bfs():
    global a, b, c
    deq = deque()
    deq.append((a, b))
    visited[a][b] = True

    while deq:
        a, b = deq.popleft()
        c = total - a - b

        if a == b == c:
            return 1

        for na, nb in ((a, b), (a, c), (b, c)):
            if na < nb:
                nb -= na
                na += na
            elif na > nb:
                na -= nb
                nb += nb
            else:
                continue

            nc = total - na - nb
            a = min(min(na, nb), nc)
            b = max(max(na, nb), nc)

            if not visited[a][b]:
                deq.append((a, b))
                visited[a][b] = True

    return 0

if total % 3 != 0:
    print(0)

else:
    print(bfs())
