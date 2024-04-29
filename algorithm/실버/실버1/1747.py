def getPrime(N):
    primes = [True for _ in range(N + 1)]
    primes[0] = False
    primes[1] = False
    p = 2
    while p*p <= N:
        if primes[p]:
            for i in range(p*p, N+1, p):
                primes[i] = False
        p += 1
    return primes

def isPalindrome(num):
    strNum = str(num)
    return strNum == strNum[::-1]

primes = getPrime(1010000)

N = int(input())

for i in range(N, 1010000+1):
    if primes[i] and isPalindrome(i):
        print(i)
        break

