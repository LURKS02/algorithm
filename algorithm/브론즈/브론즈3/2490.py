cases = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}

for i in range(3):
    l = list(map(int, input().split()))
    cn = l.count(0)
    if cn == 0:
        print(cases[5])
    elif cn == 1:
        print(cases[1])
    elif cn == 2:
        print(cases[2])
    elif cn == 3:
        print(cases[3])
    else:
        print(cases[4])