N = input()

flag = False

for i in range(1, len(N)):
    a = N[:i]
    b = N[i:]
    X = 1
    Y = 1

    for c in a:
        X *= int(c)
    for c in b:
        Y *= int(c)

    if X == Y:
        flag = True
        break

if flag:
    print('YES')
else:
    print('NO')

