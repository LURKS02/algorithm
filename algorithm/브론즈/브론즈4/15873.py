num = input()

if len(num) == 2:
    A = int(num[0])
    B = int(num[1])

    print(A + B)

elif len(num) == 3:
    A = num[:2]
    B = num[2]

    if B == '0':
        B = A[1] + B
        A = A[0]

    A = int(A)
    B = int(B)
    print(A + B)

else:
    print(20)