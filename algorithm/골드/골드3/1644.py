N = int(input())

primes = [True for _ in range(N + 1)]
p = 2

while p*p <= N:
    if primes[p]:
        for i in range(p*p, N+1, p):
            primes[i] = False
    p += 1

filtered_primes = [i for i in range(2, N+1) if primes[i] == True]

# print(filtered_primes)

currentSum = 0
start = 0
end = 0

answer = 0

while True:
    if currentSum >= N:
        currentSum -= filtered_primes[start]
        start += 1

    elif end == len(filtered_primes):
        break

    else:
        currentSum += filtered_primes[end]
        end += 1

    if currentSum == N:
        answer += 1

print(answer)
