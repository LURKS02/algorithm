N = input()

sum = 0
for num in N:
    sum += int(num)
if sum % 3 is not 0:
    print(-1)
elif '0' not in N:
    print(-1)
else:
    l = [int(digit) for digit in N]
    l.sort(reverse=True)
    for num in l:
        print(num,end='')

