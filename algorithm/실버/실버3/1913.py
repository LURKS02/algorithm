N = int(input())
find = int(input())

fx = -1
fy = -1

l = [[0] * N for i in range(N)]

mid = (N // 2) + 1

count = 1
weight = 1
direction = 1

x = mid - 1
y = mid - 1

while(x >= 0 and x < N and y >= 0 and y < N):
    for _ in range(weight):
        if count == find:
            fx = x
            fy = y
        l[x][y] = count
        count += 1
        if direction == 1:
            x -= 1
        elif direction == 2:
            y += 1
        elif direction == 3:
            x += 1
        elif direction == 4:
            y -= 1

    if direction == 1:
        direction = 2
    elif direction == 2:
        direction = 3
        weight += 1
    elif direction == 3:
        direction = 4
    elif direction == 4:
        direction = 1
        weight += 1

for m in l:
    for j in m:
        print(j, end=' ')
    print()

print(fx + 1, fy + 1, end=' ')