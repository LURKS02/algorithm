n, m = map(int, input().split())
list = []
for i in range(n):
    list.append(input())

for i in list:
    print(i[::-1])