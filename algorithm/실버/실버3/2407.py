n, m = map(int, input().split())
top = [i for i in range(n, n - m, -1)]

bottom = [i for i in range(m, 0, -1)]

topnum = 1
for num in top:
    topnum *= num

bottomnum = 1
for num in bottom:
    bottomnum *= num

print(topnum // bottomnum)

