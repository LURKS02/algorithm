import math

t = int(input())

for _ in range(t):
    l = list(map(int, input().split()))[1:]
    sum = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            sum += math.gcd(l[i], l[j])

    print(sum)