N = int(input())
P = int(input())
list = []
list.append(P)

if N >= 5:
    price = P - 500
    if price < 0:
        price = 0
    list.append(price)

if N >= 10:
    price = P // 100 * 90
    list.append(price)

if N >= 15:
    price = P - 2000
    if price < 0:
        price = 0
    list.append(price)

if N >= 20:
    price = P // 100 * 75
    list.append(price)

print(min(list))
