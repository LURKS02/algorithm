N = int(input())

l=[]

for _ in range(N):
    l.append(input())

def countX(s):
    count = 0
    inGroup = False
    length = 0

    for char in s:
        if char == '.':
            if not inGroup:
                inGroup = True
            length += 1

        else:
            if inGroup and length >= 2:
                count += 1
            inGroup = False
            length = 0

    if inGroup and length >= 2:
        count += 1
    return count

sum = 0
for i in range(N):
    sum += countX(l[i])
print(sum, end=' ')

sum = 0
for j in range(N):
    list = []
    for k in range(N):
        list.append(l[k][j])
    sum += countX(list)
print(sum, end= ' ')