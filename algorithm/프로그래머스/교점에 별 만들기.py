from itertools import combinations

def solution(line):
    answer = []

    points = set()

    for lineTuple in combinations(line, 2):
        line1, line2 = lineTuple
        A, B, E = line1[0], line1[1], line1[2]
        C, D, F = line2[0], line2[1], line2[2]

        if A*D - B*C == 0:
            continue

        xTop = B*F - E*D
        xBottom = A*D - B*C
        x = float('inf')
        if xTop % xBottom == 0:
            x = xTop // xBottom

        yTop = E*C - A*F
        yBottom = A*D - B*C
        y = float('inf')
        if yTop % yBottom == 0:
            y = yTop // yBottom

        if x != float('inf') and y != float('inf'):
            points.add((x, y))

    # print(points)
    pointList = list(points)
    maxX = -float('inf')
    maxY = -float('inf')
    minX = float('inf')
    minY = float('inf')

    for point in pointList:
        maxX = max(maxX, point[0])
        maxY = max(maxY, point[1])
        minX = min(minX, point[0])
        minY = min(minY, point[1])

    matrix = [['.'] * (maxX - minX + 1) for _ in range(maxY - minY + 1)]

    for point in pointList:
        newX, newY = point[0] - minX, point[1] - minY
        # print(newX, newY)
        matrix[newY][newX] = '*'

    returnMatrix = []
    for i in range(len(matrix)-1, -1, -1):
        returnMatrix.append(''.join(matrix[i]))

    return returnMatrix

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))