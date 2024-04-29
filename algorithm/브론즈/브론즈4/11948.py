mylist = []
mylist.append(int(input()))
mylist.append(int(input()))
mylist.append(int(input()))
mylist.append(int(input()))
mylist.append(int(input()))
mylist.append(int(input()))


listA = mylist[:4]
listB = mylist[4:]

listA.sort(reverse=True)
listB.sort(reverse=True)

total = sum(listA[:3]) + listB[0]
print(total)