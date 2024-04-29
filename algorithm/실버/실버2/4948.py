def sleve_of_eratosthenes(start, limit):
    prime = [True for _ in range(limit+1)]
    p = 2
    while p*p <= limit:
        if prime[p]:
            for i in range(p*p, limit + 1, p):
                prime[i] = False
        p += 1

    count = 0
    for i in range(start+1, limit+1):
        if prime[i]:
            count += 1
    return count

while(True):
    n = int(input())
    if n == 0:
        break
    else:
        print(sleve_of_eratosthenes(n, 2 * n))