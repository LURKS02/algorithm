N = int(input())

myList = []

X, Y = map(int, input().split())
firstX = X
firstY = Y
total = 0

for i in range(N):

    if i == N - 1:
        if abs(X - firstX) > 0:
            total += abs(newX - firstX)

        if abs(Y - firstY) > 0:
            total += abs(newY - firstY)

    else :
        newX, newY = map(int, input().split())
        if abs(newX - X) > 0:
            total += abs(newX - X)

        if abs(newY - Y) > 0:
            total += abs(newY - Y)

    X = newX
    Y = newY

print(total)
