def grade(f):
    if f >= 0 and f <= 4:
        return 1
    elif f >= 4 and f <= 11:
        return 2
    elif f >= 11 and f <= 23:
        return 3
    elif f >= 23 and f <= 40:
        return 4
    elif f >= 40 and f <= 60:
        return 5
    elif f >= 60 and f <= 77:
        return 6
    elif f >= 77 and f <= 89:
        return 7
    elif f >= 89 and f <= 96:
        return 8
    else:
        return 9

N, K = map(int, input().split())
l = list(map(int, input().split()))

for i in l:
    print(grade((i * 100) // N), end= ' ')