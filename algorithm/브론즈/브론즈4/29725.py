def count(c):
    global W
    global D

    if c == 'K':
        W += 0
    elif c == 'k':
        D += 0
    elif c == 'P':
        W += 1
    elif c == 'p':
        D += 1
    elif c == 'N':
        W += 3
    elif c == 'n':
        D += 3
    elif c == 'B':
        W += 3
    elif c == 'b':
        D += 3
    elif c == 'R':
        W += 5
    elif c == 'r':
        D += 5
    elif c == 'Q':
        W += 9
    else:
        D += 9

W = 0
D = 0

for i in range(8):
    l = input()
    for c in l:
        if c != '.':
            count(c)

print(W - D)
