while(1):
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break

    sub = B - A
    print(A - sub)
