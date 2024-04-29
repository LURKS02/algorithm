price, num, money = map(int, input().split())
total = price * num
if (money >= total):
    print(0)
else:
    print(total - money)