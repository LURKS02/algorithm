n = int(input())
bulb = list(map(int, input()))
target = list(map(int, input()))

def change(A, B):
    ACopy = A[:]
    press = 0

    for i in range(1, n):
        if ACopy[i-1] == B[i-1]:
            continue

        press += 1
        for j in range(i-1, i+2):
            if j < n:
                ACopy[j] = 1 - ACopy[j]

    if ACopy == B:
        return press
    else:
        return 1e9

res = change(bulb, target)

bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]

res = min(res, change(bulb, target) + 1)

if res != 1e9:
    print(res)
else:
    print(-1)