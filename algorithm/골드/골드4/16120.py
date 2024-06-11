stringList = list(input())

stack = []

PPAPCheck = False
for s in stringList:
    stack.append(s)
    if s == 'P':
        if PPAPCheck and stack[len(stack) - 3:] == ['P', 'A', 'P']:
            stack.pop()
            stack.pop()
            stack.pop()
        if not PPAPCheck and stack[len(stack) - 4:] == ['P', 'P', 'A', 'P']:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            PPAPCheck = True

if not stack or stringList == ['P']:
    print('PPAP')
else:
    print('NP')
