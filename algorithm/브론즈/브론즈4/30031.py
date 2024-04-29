def money(w):
    if w == 136:
        return 1000
    elif w == 142:
        return 5000
    elif w == 148:
        return 10000
    else:
        return 50000

N = int(input())

total = 0

for i in range(N):
    w, h = map(int, input().split())
    total += money(w)

print(total)