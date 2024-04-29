from itertools import combinations

while(True):
    l = list(map(int, input().split()))

    if l[0] == 0:
        break

    else:
        new = list(combinations(l[1:], 6))
        for n in new:
            print(*n)
        print()