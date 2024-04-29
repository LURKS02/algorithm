while(True):
    l = list(map(int, input().split()))
    if l[0] == 0 and l[1] == 0 and l[2] == 0:
        break

    l.sort()

    if pow(l[2], 2) == pow(l[0], 2) + pow(l[1], 2):
        print('right')
    else: print('wrong')