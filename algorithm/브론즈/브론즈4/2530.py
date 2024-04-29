import sys

h, m, s = map(int, sys.stdin.readline().strip().split())
time = int(sys.stdin.readline().strip())

a = time // 3600
time = time % 3600

b = time // 60
time = time % 60

s += time
if s >= 60:
    b += 1
    s %= 60

m += b
if m >= 60:
    a += 1
    m %= 60

h += a
if h >= 24:
    h %= 24

print(h, m, s, end=' ')