A, B, V = map(int, input().split())

if A == V:
    print(1)

else:
    total = V - A
    today = A - B

    if total % today == 0:
        print(total // today + 1)
    else:
        print(total // today + 2)

