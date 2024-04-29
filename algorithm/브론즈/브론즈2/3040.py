l = []

for i in range(9):
    l.append(int(input()))

m = sum(l) - 100

myi = -1
myj = -1

for i in range(9):
    for j in range(i+1, 9):
        if l[i] + l[j] == m:
            myi = i
            myj = j
            break

for i in range(len(l)):
    if i == myi or i == myj:
        continue
    else:
        print(l[i])
