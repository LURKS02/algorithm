str = input()

num = ''
minusstate = False
minusnums = []
plusnums = []
for c in str:
    if c.isdigit():
        num = num + c
    elif c == '-':
        realnum = int(num)
        num = ''
        if minusstate:
            minusnums.append(realnum)
        else:
            plusnums.append(realnum)
        minusstate = True

    elif c == '+':
        realnum = int(num)
        num = ''
        if minusstate:
            minusnums.append(realnum)
        else:
            plusnums.append(realnum)

if len(num) != 0:
    realnum = int(num)
    if minusstate:
        minusnums.append(realnum)
    else:
        plusnums.append(realnum)

count = 0

for num in minusnums:
    count -= num
for num in plusnums:
    count += num
print(count)