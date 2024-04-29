T = int(input())

for _ in range(T):
    N = int(input())

    fiboone = [0, 1]
    fibozero = [1, 0]

    for i in range(2, N + 1):
        fiboone.append(fiboone[i - 2] + fiboone[i - 1])
        fibozero.append(fibozero[i - 2] + fibozero[i - 1])
    print(fibozero[N], fiboone[N], end=' ')
    print()