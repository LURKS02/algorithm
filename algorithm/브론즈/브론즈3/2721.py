r = int(input())

def T(N):
    sum = 0
    for i in range(N):
        sum += i + 1
    return sum

def weight(N):
    sum = 0
    for i in range(N):
        sum += (i+1) * T(i + 2)
    return sum

for _ in range(r):
    N = int(input())
    print(weight(N))
