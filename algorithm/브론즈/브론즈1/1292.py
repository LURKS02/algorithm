A, B = map(int, input().split())

count = 0
sum = 0
for i in range(1, 1001):
    for j in range(i):
        count += 1
        if B == count:
            sum += i
            break
        elif count >= A and count < B:
            sum += i

print(sum)