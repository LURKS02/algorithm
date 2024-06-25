from copy import deepcopy

N, M, K = map(int, input().split())
stickers = []

for _ in range(K):
    R, C = map(int, input().split())

    sticker = [list(map(int, input().split())) for _ in range(R)]
    stickers.append(sticker)

notebook = [[0] * M for _ in range(N)]

def putSticker(sticker):
    N, M = len(notebook), len(notebook[0])
    R, C = len(sticker), len(sticker[0])

    if R > N or C > M:
        return False

    # for r in range(R):
    #     print(*sticker[r])
    # print()
    #
    # print(N, R, M, C)
    for i in range(N-R+1):
        for j in range(M-C+1):
            canPut = True
            # print(canPut)
            for r in range(R):
                for c in range(C):
                    if notebook[i+r][j+c] == 1 and sticker[r][c] == 1:
                        canPut = False
            if canPut:
                # print(i, j)
                for n in range(R):
                    for c in range(C):
                        if notebook[i+n][j+c] == 0:
                            notebook[i+n][j+c] = sticker[n][c]

                # for i in range(N):
                #     print(*notebook[i])
                # print()
                return True

    return False

def rotateSticker(sticker):
    R, C = len(sticker), len(sticker[0])
    tempSticker = [[0] * R for _ in range(C)]

    for i in range(R):
        for j in range(C):
            tempSticker[j][R-i-1] = sticker[i][j]
    return tempSticker

for sticker in stickers:
    tempSticker = deepcopy(sticker)
    for i in range(4):
        result = putSticker(tempSticker)
        if not result:
            tempSticker = rotateSticker(tempSticker)
        else:
            break

s = 0
for i in range(N):
    for j in range(M):
        s += notebook[i][j]

print(s)