str = list(input())

stack = []

open = []
close = []

for s in str:
    if s == "(":
        if not open:
            open.append(1)
            close.append(0)
        else:
            open.append(open[-1] + 1)
            close.append(close[-1])
    else:
        if not close:
            close.append(1)
            open.append(0)
        else:
            close.append(close[-1] + 1)
            open.append(open[-1])

if abs(open[-1] - close[-1]) != 2:
    print(0)
    exit(0)

for i in range(len(str)):
    s = str[i]
    if s == "(":
        stack.append(i)
    else:
        if stack:
            stack.pop()

        else:
            print(close[i])
            exit(0)

if stack:
    if len(stack) == 2:
        print(open[-1] - open[stack[-1] - 1])
    else:
        print(0)
else:
    print(0)


