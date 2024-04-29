import sys
input = sys.stdin.readline

prime = [True for _ in range(1000000 + 1)]

p = 2
while p*p <= 1000000:
    if prime[p]:
        for i in range(p*p, 1000000 + 1, p):
            prime[i] = False
    p += 1

for _ in range(int(input().rstrip())):
    N = int(input().rstrip())
    p = 2
    count = 0
    while p <= N // 2:
        if prime[p] and prime[N-p]:
            count += 1
        p += 1
    print(count)
