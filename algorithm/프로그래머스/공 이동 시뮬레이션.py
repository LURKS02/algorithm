
def solution(n, m, x, y, queries):
    sx, sy = x, y
    ex, ey = x, y

    for i in range(len(queries)-1, -1, -1):
        dir, dx = queries[i][0], queries[i][1]

        if dir == 0:
            nsy, ney = -1, -1
            if sy == 0:
                nsy = 0
            else:
                nsy = sy + dx
            ney = ey + dx

            if 0 <= nsy < m and 0 <= ney < m:
                sy = nsy
                ey = ney
            elif 0 <= nsy < m:
                sy = nsy
                ey = min(ney, m-1)
            else:
                return 0

        elif dir == 1:
            nsy, ney = -1, -1

            nsy = sy - dx
            if ey == m-1:
                ney = m-1
            else:
                ney = ey - dx

            if 0 <= nsy < m and 0 <= ney < m:
                sy = nsy
                ey = ney
            elif 0 <= ney < m:
                ey = ney
                sy = max(0, nsy)
            else:
                return 0

        elif dir == 2:
            nsx, nex = -1, -1
            if sx == 0:
                nsx = 0
            else:
                nsx = sx + dx
            nex = ex + dx

            if 0 <= nsx < n and 0 <= nex < n:
                sx = nsx
                ex = nex
            elif 0 <= nsx < n:
                sx = nsx
                ex = min(nex, n-1)
            else:
                return 0

        else:
            nsx, nex = -1, -1
            nsx = sx - dx
            if ex == n-1:
                nex = n-1
            else:
                nex = ex - dx

            if 0 <= nsx < n and 0 <= nex < n:
                sx = nsx
                ex = nex
            elif 0 <= nex < n:
                sx = max(0, nsx)
                ex = nex
            else:
                return 0

    return (ex - sx + 1) * (ey - sy + 1)

print(solution(2, 2, 0, 0, [[2,1],[0,1],[1,1],[0,1],[2,1]]))
print(solution(2, 5, 0, 1, [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]))
print(solution(1, 1, 0, 0, [[2,1],[0,1],[1,1],[0,1],[2,1]]))
print(solution(1000, 1000, 1, 1, [[0,100001],[2,100001]]))