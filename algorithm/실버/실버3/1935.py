N = int(input())

s = input()

dict = {}
stack = []

start = 'A'
for _ in range(N):
    dict[start] = int(input())
    start = chr(ord(start) + 1)

for c in s:
    if c == '*':
        a = stack.pop()
        b = stack.pop()
        result = a * b
        stack.append(result)
    elif c == '+':
        a = stack.pop()
        b = stack.pop()
        result = a + b
        stack.append(result)
    elif c == '/':
        a = stack.pop()
        b = stack.pop()
        result = b / a
        stack.append(result)
    elif c == '-':
        a = stack.pop()
        b = stack.pop()
        result = b - a
        stack.append(result)
    else:
        stack.append(dict[c])

print(format(stack[0], ".2f"))