T = int(input())

for _ in range(T):
    N = int(input())
    inS = set(list(map(int, input().split())))

    M = int(input())
    l = list(map(int, input().split()))

    for num in l:
        if num in inS:
            print(1)
        else:
            print(0)
