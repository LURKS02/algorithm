while(1):
    N = int(input())
    if N == 0:
        break

    sum = 0
    for i in range(N):
        sum += (i + 1) * (i + 1)

    print(sum)