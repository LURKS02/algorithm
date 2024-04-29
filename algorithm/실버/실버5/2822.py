l = []
for _ in range(8):
    l.append(int(input()))


maxList = []
sum = 0
for i in range(5):
    maxvalue = max(l)
    maxIndex = l.index(maxvalue)

    sum += maxvalue
    maxList.append(maxIndex + 1)
    l[maxIndex] = -1

maxList.sort()
print(sum)
for num in maxList:
    print(num, end= ' ')