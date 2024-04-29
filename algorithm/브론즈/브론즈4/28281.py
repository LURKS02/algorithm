N, X = map(int, input().split())

price = list(map(int, input().split()))

new = []

for i in range(len(price) - 1):
    new.append(price[i] + price[i+1])

new.sort()
print(X * new[0])

