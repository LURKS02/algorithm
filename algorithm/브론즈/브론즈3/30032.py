N, D = map(int, input().split())

def change(c, direction):
    if direction == 1:
        if c == 'd':
            return 'q'
        elif c == 'b':
            return 'p'
        elif c == 'q':
            return 'd'
        else:
            return 'b'

    else:
        if c == 'd':
            return 'b'
        elif c == 'b':
            return 'd'
        elif c == 'q':
            return 'p'
        else:
            return 'q'

for i in range(N):
    mys = input()
    newString = ''.join(change(c, D) for c in mys)
    print(newString)