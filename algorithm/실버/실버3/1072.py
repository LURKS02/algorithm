
X, Y = map(int, input().split())

Z = (Y * 100) // X
minA = 1
maxA = X

if Z >= 99:
    print(-1)
else:
    while (minA <= maxA):
        mid = (minA + maxA) // 2
        if ((Y + mid) * 100) // (X + mid) > Z:
            maxA = mid - 1
        else:
            minA = mid + 1
    print(minA)



