list = list(map(int, input().split()))

x, y, r = map(int, input().split())

min = x - r
max = x + r

trigger = False

for i in range(len(list)):
    if list[i] == x:
        trigger = True
        print(i + 1)

if trigger == False:
    print(0)