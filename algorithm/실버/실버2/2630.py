import sys
sys.setrecursionlimit(10 ** 9)

N = int(input())

l = []

for _ in range(N):
    newl = list(map(int, input().split()))
    l.append(newl)

def ispaper(x, y, i, j):
    whitecount = 0
    bluecount = 0
    for n in range(x, i + 1):
        for m in range(y, j + 1):
            if l[n][m] == 0:
                whitecount += 1
            else:
                bluecount += 1
    if whitecount == (i - x + 1) * (j - y + 1):
        return (1, 0)
    elif bluecount == (i - x + 1) * (j - y + 1):
        return (0, 1)
    else:
        return tuple(sum(x) for x in zip(ispaper(x, y, (i + x) // 2, (j + y) // 2), ispaper((i + x) // 2 + 1, y, i, (j + y) // 2), ispaper(x, (y + j) // 2 + 1, (x + i) // 2, j), ispaper((x + i) // 2 + 1, (y + j) // 2 + 1, i, j)))

total = ispaper(0, 0, N - 1, N - 1)
print(total[0])
print(total[1])
