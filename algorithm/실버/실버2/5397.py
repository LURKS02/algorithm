from collections import deque

for _ in range(int(input())):
    inputs = input()

    left_stack = deque()
    right_stack = deque()
    for c in inputs:
        if c == '<':
            if left_stack:
                right_stack.appendleft(left_stack.pop())
        elif c == '>':
            if right_stack:
                left_stack.append(right_stack.popleft())
        elif c == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(c)

    left_stack.extend(right_stack)
    print(''.join(left_stack))