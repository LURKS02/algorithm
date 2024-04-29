T = int(input())

def isVPS(str):
    stack = []
    for c in str:
        if c == '(':
            stack.append('(')
        else:
            if not stack:
                return 'NO'
            else:
                stack.pop()
    if stack:
        return 'NO'
    else:
        return 'YES'

for i in range(T):
    print(isVPS(input()))