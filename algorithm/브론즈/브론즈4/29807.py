myl = [0] * 5

N = int(input())
l = list(map(int, input().split()))
for i in range(len(l)):
    myl[i] = l[i]

A = 0
B = 0
C = 0

if myl[0] > myl[2]:
    A = (myl[0] - myl[2]) * 508
else:
    A = abs(myl[0] - myl[2]) * 108

if myl[1] > myl[3]:
    B = (myl[1] - myl[3]) * 212
else:
    B = abs(myl[1] - myl[3]) * 305

if myl[4] > 0:
    C = myl[4] * 707

t = (A + B + C) * 4763
print(t)