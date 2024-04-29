import sys
from collections import deque

while(True):
    inputLine = sys.stdin.readline().rstrip()
    if inputLine == '.':
        break
    else:
        stack = deque()

        ans = 'yes'

        for c in inputLine:
            if c == '(':
                stack.append(c)
            elif c == '[':
                stack.append(c)
            elif c == ')':
                if len(stack) == 0:
                    ans = 'no'
                    break
                elif stack[-1] == '(':
                    stack.pop()
                else:
                    ans = 'no'
                    break
            elif c == ']':
                if len(stack) == 0:
                    ans = 'no'
                    break
                elif stack[-1] == '[':
                    stack.pop()
                else:
                    ans = 'no'
                    break

        if len(stack) != 0:
            ans = 'no'
        print(ans)
