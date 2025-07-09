from collections import defaultdict
import heapq

R, C, M = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

matrix = defaultdict(list)
fisher = defaultdict(list)

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    matrix[(r-1, c-1)].append((z, s, d-1))
    heapq.heappush(fisher[c-1], r-1)

person = 0

while person < C:
    r = heapq.heappop(fisher[person])
    del matrix[r][person]

    tempMatrix = [[list() for _ in range(C)] for _ in range(R)]
    for (kr, kc) in matrix.keys():
        z, s, d = matrix[(kr, kc)]
        nr, nc = -1, -1

        if d == 1:
            if kr >= s:
                nr = kr - s
                nc = kc
            else:
                s -= kr

                h = (s-1) // (R-1)

                if h % 2 == 0:
                    temp = (s-1) % (R-1)
                    nr = temp+1
                    nc = kc
                else:





    person += 1

