start = 0

for i in range(10):
    turn = int(input())
    if turn == 1:
        start += 90
    elif turn == 2:
        start += 180
    else:
        start -= 90

    if start >= 360:
        start -= 360
    if start == -90:
        start = 270
    if start == -180:
        start = 180
    if start == -270:
        start = 90

if start == 0:
    print('N')
elif start == 90:
    print('E')
elif start == 180:
    print('S')
else:
    print('W')