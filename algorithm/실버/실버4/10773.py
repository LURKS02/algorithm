K = int(input())

total = []

for _ in range(K):
    value = int(input())
    if value == 0:
        total.pop()
    else:
        total.append(value)

print(sum(total))