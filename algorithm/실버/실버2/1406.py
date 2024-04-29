# from collections import deque
#
# d = deque(input())
# startposition = 0
# c = len(d)
#
# M = int(input())
#
# for _ in range(M):
#     inputlist = input().split()
#
#     if len(inputlist) == 1:
#         inputchar = inputlist[0]
#
#         if inputchar == 'L':
#             c -= 1
#             if c < 0:
#                 c += 1
#             else:
#                 d.rotate(1)
#                 startposition += 1
#                 if startposition >= len(d):
#                     startposition = 0
#
#         elif inputchar == 'D':
#             c += 1
#             if c > len(d):
#                 c -= 1
#             else:
#                 d.rotate(-1)
#                 startposition -= 1
#                 if startposition < 0:
#                     startposition = len(d) - 1
#
#         elif inputchar == 'B':
#             if c != 0:
#                 if startposition == len(d) - 1:
#                     startposition = 0
#                 c -= 1
#                 d.pop()
#
#     else:
#         inputchar = inputlist[1]
#
#         if startposition == 0 and c == 0:
#             startposition = len(d)
#         c += 1
#         d.appendleft(inputchar)
#         d.rotate(-1)
#
#
#     # print(inputlist)
#     # print(f'd: {d}')
#     # print(f'sp : {startposition}')
#     # print(f'c : {c}')
#     # print()
#
# l = list(d)
# for i in range(startposition, len(l)):
#     print(l[i], end='')
#
# for i in range(0, startposition):
#     print(l[i], end='')

from sys import stdin, stdout
from collections import deque
input = stdin.readline
print = stdout.write
q = deque(i for i in input().rstrip())
head = 0

for _ in range(int(input())):
    op = input()
    if op[0] == 'L':
        if head < len(q):
            q.rotate(1) # q.appendleft(q.pop())
            head += 1
    elif op[0] == 'D':
        if head > 0:
            q.rotate(-1) # q.append(q.popleft())
            head -= 1
    elif op[0] == 'B':
        if head < len(q):
            q.pop()
    else:
        q.append(op[2])
l = list(q)
for i in range(head,len(l)): print(l[i])
for i in range(head): print(l[i])