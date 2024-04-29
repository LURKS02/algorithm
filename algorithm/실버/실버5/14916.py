n = int(input())

a = n // 5
b = n % 5

while(True):
    if a == 0:
        if b % 2 == 0:
            print(b // 2)
        else:
            print(-1)
        break

    elif b % 2 == 0:
        print(a + (b // 2))
        break
    else:
        a -= 1
        b += 5
