import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

stack = [int(input())]
maxNum = stack[-1]

for _ in range(n-1):
    num = int(input())
    if stack[-1] < num:
        cnt += num - stack[-1]
        maxNum = max(maxNum, num)
    stack.pop()
    stack.append(num)
cnt += maxNum * len(stack) - sum(stack)
print(cnt)
