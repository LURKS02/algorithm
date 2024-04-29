T = int(input())

for i in range(T):
    mon = int(input())

    a = mon // 25
    mon %= 25

    b = mon // 10
    mon %= 10

    c = mon // 5
    mon %= 5

    d = mon

    print(a, b, c, d, end= ' ')
    print()