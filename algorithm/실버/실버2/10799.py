from collections import deque

stick = input()

d = deque()

stickcount = 0
totalcount = 0
for i in range(len(stick)):
    if stick[i] == '(':
        stickcount += 1
    else:
        if i != 0 and stick[i-1] == '(':
            stickcount -= 1
            totalcount += stickcount
        else:
            totalcount += 1
            stickcount -= 1

print(totalcount)