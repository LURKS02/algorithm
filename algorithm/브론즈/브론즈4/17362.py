n = int(input())

A = n % 8

if A == 1:
    print(1)
elif A == 2 or A == 0:
    print(2)
elif A == 3 or A == 7:
    print(3)
elif A == 4 or A == 6:
    print(4)
elif A == 5:
    print(5)