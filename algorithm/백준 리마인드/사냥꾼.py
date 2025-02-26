import bisect

M, N, L = map(int, input().split())
spots = list(map(int, input().split()))
spots.sort()
animals = []

for _ in range(N):
    x, y = map(int, input().split())
    animals.append((x, y))

answer = 0
for ax, ay in animals:
    a = ax
    b = L - ay
    top = a + b
    bottom = a - b

    idx = bisect.bisect_left(spots, ax)
    if idx == 0:
        if bottom <= spots[0] <= top:
            answer += 1

    elif idx == len(spots):
        if bottom <= spots[-1] <= top:
            answer += 1

    else:
        if bottom <= spots[idx-1] <= top:
            answer += 1
        elif bottom <= spots[idx] <= top:
            answer += 1

print(answer)