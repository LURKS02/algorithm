import sys
T = int(sys.stdin.readline().strip())

for i in range(T):
    a, b = map(int, sys.stdin.readline().strip().split())
    if a % 10 == 1:
        print(1)
    elif a % 10 == 2:
        l = [6, 2, 4, 8]
        print(l[b % 4])
    elif a % 10 == 3:
        l = [1, 3, 9, 7]
        print(l[b % 4])
    elif a % 10 == 4:
        l = [6, 4]
        print(l[b % 2])
    elif a % 10 == 5:
        print(5)
    elif a % 10 == 6:
        print(6)
    elif a % 10 == 7:
        l = [1, 7, 9, 3]
        print(l[b % 4])
    elif a % 10 == 8:
        l = [6, 8, 4, 2]
        print(l[b % 4])
    elif a % 10 == 9:
        l = [1, 9]
        print(l[b % 2])
    else:
        print(10)