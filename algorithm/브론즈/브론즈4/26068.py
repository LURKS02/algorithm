N = int(input())
list = []

for i in range(N):
    list.append(int(input()[2:]))

total = 0
for k in list:
    if k <= 90:
        total += 1

print(total)