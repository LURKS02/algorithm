ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())
cx1, cy1, cx2, cy2 = map(int, input().split())
dx1, dy1, dx2, dy2 = map(int, input().split())

l = [[0 for _ in range(101)] for _ in range(101)]

for i in range(ax1, ax2):
    for j in range(ay1, ay2):
        l[i][j] = 1

for i in range(bx1, bx2):
    for j in range(by1, by2):
        l[i][j] = 1

for i in range(cx1, cx2):
    for j in range(cy1, cy2):
        l[i][j] = 1

for i in range(dx1, dx2):
    for j in range(dy1, dy2):
        l[i][j] = 1

sum = 0
for i in range(101):
    for j in range(101):
        if l[i][j] == 1:
            sum += 1

print(sum)