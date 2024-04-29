N = int(input())

onedp = [0, 1, 0]
zerodp = [0, 0, 1]

def getDP(N):
    if N == 1:
        return onedp[1] + zerodp[1]
    elif N == 2:
        return onedp[2] + zerodp[2]
    else:
        for i in range(3, N + 1):
            onedp.append(zerodp[i - 1])
            zerodp.append(onedp[i-1] + zerodp[i-1])
    return onedp[N] + zerodp[N]

print(getDP(N))