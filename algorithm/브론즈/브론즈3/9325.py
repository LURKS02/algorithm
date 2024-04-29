T = int(input())

for i in range(T):
    car = int(input())
    N = int(input())

    optionSum = 0
    for i in range(N):
        q, p = map(int, input().split())
        optionSum += q * p

    print(car + optionSum)