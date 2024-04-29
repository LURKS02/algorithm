N = int(input())
l = list(map(int, input().split()))

my = 0
start = 0
high = []
m = 0
for n in l:
    if n > my:
        high.append(n)
    else:
        if len(high) >= 2:
            m = max(m, high[len(high)-1] - high[0])
        high = [n]
    my = n

if len(high) >= 2:
    m = max(m, high[len(high) - 1] - high[0])

print(m)