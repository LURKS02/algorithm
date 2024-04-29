N = int(input())

d = 0
p = 0

for i in range(N):
    win = input()
    if win == 'D':
        d += 1
    else:
        p += 1

    if abs(d - p) == 2:
        break

print(f'{d}:{p}')