from collections import deque

T = int(input())

def bfs(visited, n, m, count, x, y):
    if not visited[n][m]:

        deq = deque()
        deq.append((n, m, count))

        while(deq):
            position = deq.popleft()
            positionn = position[0]
            positionm = position[1]
            positioncount = position[2]

            if positionn == x and positionm == y:
                print(positioncount)
                break

            if positionn >= 0 and positionm >= 0 and positionn < len(visited) and positionm < len(visited) and not visited[positionn][positionm]:
                visited[positionn][positionm] = True

                deq.append((positionn-2, positionm-1, positioncount+1))
                deq.append((positionn-1, positionm-2, positioncount+1))
                deq.append((positionn+1, positionm-2, positioncount+1))
                deq.append((positionn+2, positionm-1, positioncount+1))
                deq.append((positionn-2, positionm+1, positioncount+1))
                deq.append((positionn-1, positionm+2, positioncount+1))
                deq.append((positionn+1, positionm+2, positioncount+1))
                deq.append((positionn+2, positionm+1, positioncount+1))

            #print(deq)

for _ in range(T):
    I = int(input())
    a, b = map(int, input().split())
    x, y = map(int, input().split())

    visited = [[False for _ in range(I)] for _ in range(I)]

    bfs(visited, a, b, 0, x, y)