import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
S = deque()
for _ in range(N):
    S.append(input().rstrip())

T = ""
cnt = 0

for i in range(N):
    start = 0
    end = len(S) - 1
    answer = False

    while start <= end:
        # print(start, end)
        if ord(S[start]) > ord(S[end]):
            answer = False
            break
        elif ord(S[start]) < ord(S[end]):
            answer = True
            break
        else:
            start += 1
            end -= 1

    if answer == False:
        T += S.pop()
    elif answer == True:
        T += S.popleft()

    cnt += 1
    if cnt % 80 == 0:
        T += '\n'

print(T)