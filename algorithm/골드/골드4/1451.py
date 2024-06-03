N, M = map(int, input().split())

rectangles = [[0 for _ in range(M+1)]]

for _ in range(N):
    l = [0] + list(map(int, list(input())))
    rectangles.append(l)

ans = 0

s = [[0 for _ in range(M+1)] for _ in range(N+1)]

for row in range(1, N+1):
    for col in range(1, M+1):
        s[row][col] = s[row-1][col] + s[row][col-1] - s[row-1][col-1] + rectangles[row][col]

def sumCal(x1, y1, x2, y2):
    return s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1]

for i in range(1, M-1):
    for j in range(i+1, M):
        r1 = sumCal(1, 1, N, i)
        r2 = sumCal(1, i+1, N, j)
        r3 = sumCal(1, j+1, N, M)

        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

for i in range(1, N-1):
    for j in range(i+1, N):
        r1 = sumCal(1, 1, i, M)
        r2 = sumCal(i+1, 1, j, M)
        r3 = sumCal(j+1, 1, N, M)

        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

for i in range(1, M):
    for j in range(1, N):
        r1 = sumCal(1, 1, N, i)
        r2 = sumCal(1, i+1, j, M)
        r3 = sumCal(j+1, i+1, N, M)

        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

for i in range(1, N):
    for j in range(1, M):
        r1 = sumCal(1, 1, i, j)
        r2 = sumCal(i+1, 1, N, j)
        r3 = sumCal(1, j+1, N, M)

        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

for i in range(1, N):
    for j in range(1, M):
        r1 = sumCal(1, 1, i, M)
        r2 = sumCal(i+1, 1, N, j)
        r3 = sumCal(i+1, j+1, N, M)

        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

for i in range(1, N):
    for j in range(1, M):
        r1 = sumCal(1, 1, i, j)
        r2 = sumCal(1, j+1, i, M)
        r3 = sumCal(i+1, 1, N, M)

        if ans < r1 * r2 * r3:
            ans = r1 * r2 * r3

print(ans)