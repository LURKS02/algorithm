def f(n, a, b, c):
    if n == 1:
        print(a, c, sep=' ')

    else:
        f(n-1, a, c, b)
        f(1, a, b, c)
        f(n-1, b, a, c)

N = int(input())
print(2**N-1)
if N <= 20:
    f(N, 1, 2, 3)