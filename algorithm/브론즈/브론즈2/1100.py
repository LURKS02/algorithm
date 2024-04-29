count = 0
for i in range(8):
    l = input()
    if i % 2 == 0:
        isWhite = True
    else:
        isWhite = False

    for c in l:
        if isWhite and c == 'F':
            count += 1
        isWhite = not isWhite

print(count)