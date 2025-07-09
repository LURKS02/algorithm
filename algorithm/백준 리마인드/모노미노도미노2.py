N = int(input())

blueBoard = [[0] * 6 for _ in range(4)]
greenBoard = [[0] * 4 for _ in range(6)]

score = 0

def putBlock(block, x, y):
    if block == 1:
        # blue
        target = -1
        for i in range(6):
            if blueBoard[x][i] == 0:
                target = i
            else:
                break
        blueBoard[x][target] = 1

        # green
        target = -1
        for i in range(6):
            if greenBoard[i][y] == 0:
                target = i
            else:
                break
        greenBoard[target][y] = 1

    elif block == 2:
        # blue
        target = -1
        for i in range(6):
            if blueBoard[x][i] == 0:
                target = i
            else:
                break
        blueBoard[x][target] = 1
        blueBoard[x][target-1] = 1

        #green
        target = -1
        for i in range(6):
            if greenBoard[i][y] == 0 and greenBoard[i][y+1] == 0:
                target = i
            else:
                break
        greenBoard[target][y] = 1
        greenBoard[target][y+1] = 1

    elif block == 3:
        # blue
        target = -1
        for i in range(6):
            if blueBoard[x][i] == 0 and blueBoard[x+1][i] == 0:
                target = i
            else:
                break
        blueBoard[x][target] = 1
        blueBoard[x+1][target] = 1

        # green
        target = -1
        for i in range(6):
            if greenBoard[i][y] == 0:
                target = i
            else:
                break
        greenBoard[target][y] = 1
        greenBoard[target-1][y] = 1

def checkBlocks():
    global score

    # blue
    haveToRemove = set()

    # 열
    for i in range(6):
        flag = True
        for j in range(4):
            if blueBoard[j][i] != 1:
                flag = False
                break

        if flag:
            haveToRemove.add(i)

    blueScore = len(haveToRemove)
    pf = 0
    for j in range(5, -1, -1):
        if j in haveToRemove:
            pf += 1
        else:
            if pf == 0:
                continue
            else:
                for i in range(4):
                    blueBoard[i][j+pf] = blueBoard[i][j]
                for i in range(4):
                    blueBoard[i][j] = 0

    # green
    haveToRemove = set()

    # 행
    for i in range(6):
        flag = True
        for j in range(4):
            if greenBoard[i][j] != 1:
                flag = False
                break

        if flag:
            haveToRemove.add(i)

    greenScore = len(haveToRemove)
    pf = 0
    for i in range(5, -1, -1):
        if i in haveToRemove:
            pf += 1
        else:
            if pf == 0:
                continue
            else:
                for j in range(4):
                    greenBoard[i+pf][j] = greenBoard[i][j]
                for j in range(4):
                    greenBoard[i][j] = 0

    score += blueScore
    score += greenScore

def moveBlocks():
    # blue
    stack = 0

    for j in range(2):
        flag = False
        for i in range(4):
            if blueBoard[i][j] != 0:
                flag = True
                break

        if flag:
            stack += 1

    if stack != 0:
        for j in range(5 - stack, -1, -1):
            for i in range(4):
                blueBoard[i][j+stack] = blueBoard[i][j]
                blueBoard[i][j] = 0

    # green
    stack = 0

    for i in range(2):
        flag = False
        for j in range(4):
            if greenBoard[i][j] != 0:
                flag = True
                break

        if flag:
            stack += 1

    if stack != 0:
        for i in range(5 - stack, -1, -1):
            for j in range(4):
                greenBoard[i+stack][j] = greenBoard[i][j]
                greenBoard[i][j] = 0

def countBlocks():
    count = 0

    for i in range(4):
        for j in range(6):
            if blueBoard[i][j] == 1:
                count += 1
            if greenBoard[j][i] == 1:
                count += 1

    return count

for _ in range(N):
    t, x, y = map(int, input().split())

    putBlock(t, x, y)

    checkBlocks()

    moveBlocks()

    # for i in range(4):
    #     print(*blueBoard[i])
    #
    # print()
    #
    # for i in range(6):
    #     print(*greenBoard[i])


print(score)
print(countBlocks())
