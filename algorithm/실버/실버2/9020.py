import sys

def get_prime(limit):
    p = 2
    l = [True] * (limit+1)
    while(p * p <= limit):
        for i in range(p*p, limit+1, p):
            l[i] = False
        p += 1

    min = 99999
    mi = -1
    mli = -1
    for i in range(2, limit + 1):
        if l[i] == True and l[limit-i] == True:
            if i > limit - i:
                break
            if min > abs(i - (limit - i)):
                min = abs(i - (limit - i))
                mi = i
                mli = limit - i


    print(mi, mli, end=' ')
    print()

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    get_prime(n)