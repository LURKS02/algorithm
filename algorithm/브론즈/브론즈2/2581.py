import math

M = int(input())
N = int(input())

def prime(N):
    if N == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                return False

        return True

l = []
for i in range(M, N + 1):
    if prime(i):
        l.append(i)

if len(l) > 0:
    print(sum(l))
    print(l[0])
else:
    print(-1)
