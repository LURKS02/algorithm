N = int(input())

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

newList = [i1 - i2 for i1, i2 in zip(list1, list2)]

total = 0
for num in newList:
    if num < 0:
        total += num

print (abs(total))