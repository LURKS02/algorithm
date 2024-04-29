sum = 0
sum2 = 0
l = []

for i in range(10):
    l.append(int(input()))

for i in range(10):
    sum += l[i]
    if sum > 100:
        sum2 = sum - l[i]
        break

if abs(100 - sum) < abs(100 - sum2):
    print(sum)
elif abs(100 - sum) > abs(100 - sum2):
    print(sum2)
else:
    print(max(sum, sum2))