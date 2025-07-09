from copy import deepcopy

T = int(input())

def getRotation(side, direction):
    if direction == "+":
        tempSide = [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]]
        for i in range(3):
            for j in range(3):
                tempSide[j][2 - i] = side[i][j]

        return tempSide

    else:
        tempSide = [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]]
        for i in range(3):
            for j in range(3):
                tempSide[2-j][i] = side[i][j]

        return tempSide

def rotateFirst(side, cube, direction):
    sides = [[[2, 0, 0, 0], [4, 0, 0, 0], [3, 0, 0, 0], [5, 0, 0, 0], [2, 0, 0, 0]],
             [[2, 2, 0, 0], [5, 2, 0, 0], [3, 2, 0, 0], [4, 2, 0, 0], [2, 2, 0, 0]],
             [[0, 2, 0, 0], [5, 0, 1, 0], [1, 0, 0, -1], [4, 2, 1, -1], [0, 2, 0, 0]],
             [[0, 0, 0, 0], [4, 0, 1, -1], [1, 2, 0, -1], [5, 2, 1, 0], [0, 0, 0, 0]],
             [[0, 0, 1, 0], [2, 0, 1, 0], [1, 0, 1, 0], [3, 2, 1, -1], [0, 0, 1, 0]],
             [[0, 2, 1, 0], [3, 0, 1, -1], [1, 2, 1, 0], [2, 2, 1, 0], [0, 2, 1, 0]]
            ]

    sideLine = sides[side]
    tempCube = deepcopy(cube)

    if direction == "+":
        # 정방향
        for i in range(1, len(sideLine)):
            copySide = sideLine[i-1][0]
            targetSide = sideLine[i][0]
            copyLine = sideLine[i-1][1]
            targetLine = sideLine[i][1]
            copyDirection = sideLine[i-1][2]
            targetDirection = sideLine[i][2]
            copyFlag = sideLine[i-1][3]
            targetFlag = sideLine[i][3]

            if copyDirection == targetDirection:
                if copyDirection == 0:
                    if copyFlag == targetFlag:
                        tempCube[targetSide][targetLine] = cube[copySide][copyLine]
                    else:
                        tempCube[targetSide][targetLine] = reversed(cube[copySide][copyLine])
                else:
                    if copyFlag == targetFlag:
                        for i in range(3):
                            tempCube[targetSide][i][targetLine] = cube[copySide][i][copyLine]
                    else:
                        for i in range(3):
                            tempCube[targetSide][i][targetLine] = cube[copySide][2-i][copyLine]
            else:
                if copyDirection == 1 and targetDirection == 0:
                    if copyFlag == targetFlag:
                        for i in range(3):
                            tempCube[targetSide][targetLine][i] = cube[copySide][i][copyLine]

                    else:
                        for i in range(3):
                            tempCube[targetSide][targetLine][i] = cube[copySide][2-i][copyLine]
                elif copyDirection == 0 and targetDirection == 1:
                    if copyFlag == targetFlag:
                        for i in range(3):
                            tempCube[targetSide][i][targetLine] = cube[copySide][copyLine][i]
                    else:
                        for i in range(3):
                            tempCube[targetSide][i][targetLine] = cube[copySide][copyLine][2-i]

    else:
        # 역방향
        for i in range(len(sideLine)-1, 0, -1):
            copySide = sideLine[i][0]
            targetSide = sideLine[i-1][0]
            copyLine = sideLine[i][1]
            targetLine = sideLine[i-1][1]
            copyDirection = sideLine[i][2]
            targetDirection = sideLine[i-1][2]
            copyFlag = sideLine[i][3]
            targetFlag = sideLine[i-1][3]

            if copyDirection == targetDirection:
                if copyDirection == 0:
                    if copyFlag == targetFlag:
                        tempCube[targetSide][targetLine] = cube[copySide][copyLine]
                    else:
                        tempCube[targetSide][targetLine] = reversed(cube[copySide][copyLine])
                else:
                    if copyFlag == targetFlag:
                        for i in range(3):
                            tempCube[targetSide][i][targetLine] = cube[copySide][i][copyLine]
                    else:
                        for i in range(3):
                            tempCube[targetSide][i][targetLine] = cube[copySide][2 - i][copyLine]
            else:
                if copyDirection == 1 and targetDirection == 0:
                    if copyFlag == targetFlag:
                        for i in range(3):
                            tempCube[targetSide][targetLine][i] = cube[copySide][i][copyLine]

                    else:
                        for i in range(3):
                            tempCube[targetSide][targetLine][i] = cube[copySide][2 - i][copyLine]
                elif copyDirection == 0 and targetDirection == 1:
                    if copyFlag == targetFlag:
                        for i in range(3):
                            tempCube[targetSide][i][targetLine] = cube[copySide][copyLine][i]
                    else:
                        for i in range(3):
                            tempCube[targetSide][i][targetLine] = cube[copySide][copyLine][2 - i]

    return tempCube

for _ in range(T):
    cube = [[['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']], # 0 = 윗면
            [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']], # 1 = 아랫면
            [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']], # 2 = 앞면
            [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']], # 3 = 뒷면
            [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']], # 4 = 왼쪽면
            [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]  # 5 = 오른쪽면
            ]

    n = int(input())
    sorting = list(input().split())

    for sort in sorting:
        side = sort[0]
        direction = sort[1]

        if side == "U":
            tempSide = getRotation(cube[0], direction)
            cube[0] = tempSide

            cube = rotateFirst(0, cube, direction)

        elif side == "D":
            tempSide = getRotation(cube[1], direction)
            cube[1] = tempSide

            cube = rotateFirst(1, cube, direction)

        elif side == "F":
            tempSide = getRotation(cube[2], direction)
            cube[2] = tempSide

            cube = rotateFirst(2, cube, direction)

        elif side == "B":
            tempSide = getRotation(cube[3], direction)
            cube[3] = tempSide

            cube = rotateFirst(3, cube, direction)

        elif side == "L":
            tempSide = getRotation(cube[4], direction)
            cube[4] = tempSide

            cube = rotateFirst(4, cube, direction)

        elif side == "R":
            tempSide = getRotation(cube[5], direction)
            cube[5] = tempSide

            cube = rotateFirst(5, cube, direction)

    for i in range(3):
        print("".join(cube[0][i]))