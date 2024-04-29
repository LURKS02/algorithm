from collections import deque

prime = [True for _ in range(10001)]
p = 2

while p * p <= 10000:
    if prime[p]:
        for i in range(p*p, 10001, p):
            prime[i] = False
    p += 1

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    toPrime = [-1 for _ in range(10001)]
    deq = deque([(A, 0)])
    toPrime[A] = 0
    answer = False

    while deq:
        num, count = deq.popleft()

        if num == B:
            print(count)
            answer = True
            break

        for i in range(1, 10):
            if i != num // 1000:
                newnum = num % 1000 + i * 1000
                if prime[newnum] and toPrime[newnum] == -1:
                    deq.append((newnum, count + 1))
                    toPrime[newnum] = count + 1

        for i in range(0, 10):
            if i != (num // 100) % 10:
                newnum = num // 1000 * 1000 + i * 100 + num % 100
                if prime[newnum] and toPrime[newnum] == -1:
                    deq.append((newnum, count + 1))
                    toPrime[newnum] = count + 1

            if i != (num // 10) % 100:
                newnum = num // 100 * 100 + i * 10 + num % 10
                if prime[newnum] and toPrime[newnum] == -1:
                    deq.append((newnum, count + 1))
                    toPrime[newnum] = count + 1

            if i != num % 10:
                newnum = num // 10 * 10 + i
                if prime[newnum] and toPrime[newnum] == -1:
                    deq.append((newnum, count + 1))
                    toPrime[newnum] = count + 1

    if not answer:
        print('Impossible')


