N, M = map(int, input().split())

l = []
for _ in range(N):
    newl = input()
    l.append(newl)

biggest = min(N, M)

def checkifisgood(x1, x2, y1, y2):
    if l[x1][x2] == l[x1][y2] == l[y1][x2] == l[y1][y2]:
        return True
    else:
        return False

for i in range(biggest, 0, -1):
    x1 = 0
    x2 = 0
    y1 = x1 + i - 1
    y2 = x2 + i - 1
    breakpoint = False
    while(y1 < N):
        if checkifisgood(x1, x2, y1, y2):
            print(pow(i, 2))
            breakpoint = True
            break
        x2 += 1
        y2 += 1
        if y2 >= M:
            x1 += 1
            x2 = 0
            y1 += 1
            y2 = i - 1
    if breakpoint:
        break


