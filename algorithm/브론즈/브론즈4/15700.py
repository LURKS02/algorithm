N, M = map(int, input().split())

if N == 1:
    if M == 1:
        print(0)
    else:
        print(M // 2)

else:
    maxVer = N // 2 * M
    if (N % 2 == 0):
        maxHor = 0
    else:
        maxHor = M // 2
    print(maxVer + maxHor)