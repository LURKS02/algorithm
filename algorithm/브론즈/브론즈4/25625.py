x, y = map(int, input().split())

if x > y:
    print(x + y)
elif x == y:
    print(0)
else:
    print(y - x)