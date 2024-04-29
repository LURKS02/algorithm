N = int(input())

for i in range(N):
    lA = list(map(int, input().split()))[1:]
    lB = list(map(int, input().split()))[1:]
    a4 = lA.count(4)
    b4 = lB.count(4)
    a3 = lA.count(3)
    b3 = lB.count(3)
    a2 = lA.count(2)
    b2 = lB.count(2)
    a1 = lA.count(1)
    b1 = lB.count(1)

    if a4 > b4:
        print('A')
    elif a4 < b4:
        print('B')
    elif a3 > b3:
        print('A')
    elif a3 < b3:
        print('B')
    elif a2 > b2:
        print('A')
    elif a2 < b2:
        print('B')
    elif a1 > b1:
        print('A')
    elif a1 < b1:
        print('B')
    else:
        print('D')
