T = int(input())

for _ in range(T):
    N, D = map(int, input().split())
    sum = 0

    for i in range(N):
        v, f, c = map(int, input().split())
        if v * (f / c) >= D:
            sum += 1

    print(sum)