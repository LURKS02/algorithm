from collections import deque

A, B, C = map(int, input().split())

def bfs():
    deq = deque([(0, 0, C)])
    visited = [[[False for _ in range(201)] for _ in range(201)] for _ in range(201)]
    visited[0][0][C] = True

    ans = set()

    while(deq):
        a, b, c = deq.popleft()

        if a == 0 and c not in ans:
            ans.add(c)

        if a > 0:
            if a + b > B:
                newA = a + b - B
                newB = B
                if not visited[newA][newB][c]:
                    visited[newA][newB][c] = True
                    deq.append((newA, newB, c))
            else:
                newA = 0
                newB = a + b
                if not visited[newA][newB][c]:
                    visited[newA][newB][c] = True
                    deq.append((newA, newB, c))

            if a + c > C:
                newA = a + c - C
                newC = C
                if not visited[newA][b][newC]:
                    visited[newA][b][newC] = True
                    deq.append((newA, b, newC))

            else:
                newA = 0
                newC = a + c
                if not visited[newA][b][newC]:
                    visited[newA][b][newC] = True
                    deq.append((newA, b, newC))

        if b > 0:
            if a + b > A:
                newA = A
                newB = a + b - A
                if not visited[newA][newB][c]:
                    visited[newA][newB][c] = True
                    deq.append((newA, newB, c))
            else:
                newA = a + b
                newB = 0
                if not visited[newA][newB][c]:
                    visited[newA][newB][c] = True
                    deq.append((newA, newB, c))

            if b + c > C:
                newB = b + c - C
                newC = C
                if not visited[a][newB][newC]:
                    visited[a][newB][newC] = True
                    deq.append((a, newB, newC))

            else:
                newB = 0
                newC = b + c
                if not visited[a][newB][newC]:
                    visited[a][newB][newC] = True
                    deq.append((a, newB, newC))

        if c > 0:
            if a + c > A:
                newA = A
                newC = a + c - A
                if not visited[newA][b][newC]:
                    visited[newA][b][newC] = True
                    deq.append((newA, b, newC))
            else:
                newA = a + c
                newC = 0
                if not visited[newA][b][newC]:
                    visited[newA][b][newC] = True
                    deq.append((newA, b, newC))

            if b + c > B:
                newB = B
                newC = b + c - B
                if not visited[a][newB][newC]:
                    visited[a][newB][newC] = True
                    deq.append((a, newB, newC))

            else:
                newB = b + c
                newC = 0
                if not visited[a][newB][newC]:
                    visited[a][newB][newC] = True
                    deq.append((a, newB, newC))

        # print(deq)

    # ans.remove(0)
    print(*sorted(list(ans)))

bfs()