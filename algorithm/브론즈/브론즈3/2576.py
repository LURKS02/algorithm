sum = 0
min = 101
for i in range(7):
    nm = int(input())
    if nm % 2 == 1:
        sum += nm
        if nm < min:
            min = nm

if sum == 0 and min == 101:
    print(-1)
else :
    print(sum)
    print(min)