import sys
input = sys.stdin.readline

N, H = map(int, input().rstrip().split())

down = [0] * H
up = [0] * H

for i in range(N):
    high = int(input().rstrip())

    if i % 2 == 0:
        down[high-1] += 1
    else:
        up[high-1] += 1

for i in range(H - 2, -1, -1):
    down[i] += down[i+1]
    up[i] += up[i+1]

# print(down)
# print(up)

min_count = N
same_height = 0

for i in range(H):
    if (min_count > down[i] + up[H - i - 1]):
        min_count = down[i] + up[H - i - 1]
        same_height = 1

    elif (min_count == down[i] + up[H - i - 1]):
        same_height += 1

print(min_count, same_height)
