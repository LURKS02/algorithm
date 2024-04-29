from collections import deque

S = input()

stack = deque()

stringstack = []
for c in S:
    if c == '<':
        if len(stringstack) != 0:
            for i in range(len(stringstack) - 1, -1, -1):
                print(stringstack[i], end='')
        stringstack = []
        stack.append('<')
        stringstack.append('<')
    elif c == '>':
        stack.pop()
        stringstack.append('>')
        print(''.join(stringstack), end='')
        stringstack = []

    elif c == ' ':
        if len(stack) == 0:
            if len(stringstack) != 0:
                for i in range(len(stringstack) - 1, -1, -1):
                    print(stringstack[i], end='')
                print(' ', end='')
            stringstack = []

        else:
            stringstack.append(' ')

    else:
        stringstack.append(c)
if len(stringstack) > 0:
    for i in range(len(stringstack) - 1, -1, -1):
        print(stringstack[i], end='')