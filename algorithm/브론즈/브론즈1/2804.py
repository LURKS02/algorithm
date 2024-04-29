A, B = input().split()

minA = -1
minB = -1

for i in range(len(A)):
    if minA != -1 and minB != -1:
        break

    for j in range(len(B)):
        if A[i] == B[j]:
            minA = i
            minB = j
            break

for i in range(len(B)):
    if i == minB:
        print(A)
    else:
        print('.' * minA + B[i] + '.' * (len(A) - 1 - minA))


