a, b = map(int, input().split())

total = a * b

list = list(map(int, input().split()))
for i in list:
    print(i - total, end= ' ')