A, B = map(int, input().split())
K, X = map(int, input().split())


max = K + X
min = K - X

l = [x for x in range(A, B + 1) if x >= min and x <= max]
if len(l) == 0:
    print('IMPOSSIBLE')
else:
    print(len(l))