N = int(input())

def getN(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        dp1 = 1
        dp2 = 2
        for i in range(3, N + 1):
            newnum = (dp2 + dp1) % 15746
            dp1, dp2 = dp2, newnum
        return newnum

print(getN(N))