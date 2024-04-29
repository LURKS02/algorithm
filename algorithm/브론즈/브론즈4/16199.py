myY, myM, myD = map(int, input().split())
Y, M, D = map(int, input().split())

yy = Y - myY
if yy > 0:
    if (myM < M):
        print(yy)
    elif (myM == M):
        if (myD <= D):
            print(yy)
        else:
            print(yy - 1)
    else:
        print(yy - 1)

else:
    print(0)

print(Y - myY + 1)
print(Y - myY)