a, b = map(int, input().split())
dep = a * (100 - b) / 100
if dep >= 100:
    print(0)
else:
    print(1)