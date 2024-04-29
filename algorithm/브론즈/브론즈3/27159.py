N = int(input())
list = list(map(int, input().split()))

minlist = []
mylist = []

for i in range(len(list)):
    if i == 0:
        mylist.append(list[i])

    elif list[i] - list[i - 1] == 1:
        continue
    else:
        mylist.append(list[i])

print(sum(mylist))

