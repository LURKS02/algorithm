import sys
input = sys.stdin.readline

def sleveOfEratosthenes(maxNum):
    isPrime = [False, False] + [True] * (maxNum - 1)
    for i in range(2, int(maxNum**0.5) + 1):
        if isPrime[i]:
            for j in range(i*2, maxNum+1, i):
                isPrime[j] = False
    return isPrime

def goldbach(n, primes):
    for i in range(3, n // 2 + 1, 2):
        if primes[i] and primes[n - i]:
            return i, n-i
    return None, None

primes = sleveOfEratosthenes(1000000)

while(True):
    n = int(input().rstrip())
    if n == 0:
        break

    a, b = goldbach(n, primes)

    if a and b:
        print(f"{n} = {a} + {b}")
    else:
        print("Goldbach's conjecture is wrong.")