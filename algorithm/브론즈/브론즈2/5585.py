M = 1000 - int(input())

count = 0

count += M // 500
M %= 500

count += M // 100
M %= 100

count += M // 50
M %= 50

count += M // 10
M %= 10

count += M // 5
M %= 5

count += M // 1
M %= 1

print(count)
