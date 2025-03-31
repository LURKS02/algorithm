from collections import deque

N = int(input())
A = list(map(int, input().split()))

stack = []

answer = deque()

for i in range(N-1, -1, -1):
    if i == N-1:
        answer.append(-1)
        stack.append(A[i])
    else:
        if A[i] < stack[-1]:
            answer.appendleft(stack[-1])
            stack.append(A[i])
        else:
            while stack and A[i] >= stack[-1]:
                stack.pop()
            if not stack:
                answer.appendleft(-1)
                stack.append(A[i])
            else:
                answer.appendleft(stack[-1])
                stack.append(A[i])

print(*answer)
