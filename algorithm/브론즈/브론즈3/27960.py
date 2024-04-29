A, B = map(int, input().split())

gradeList = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

myA = A
myB = B

al = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bl = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while(myA > 0):
    for i in reversed(range(len(gradeList))):
        if (myA - gradeList[i]) >= 0:
            myA -= gradeList[i]
            al[i] = 1

while(myB > 0):
    for i in reversed(range(len(gradeList))):
        if (myB - gradeList[i]) >= 0:
            myB -= gradeList[i]
            bl[i] = 1

cl = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(10):
    if al[i] != bl[i]:
        cl[i] = 1

sum = 0
for i in range(10):
    if cl[i] == 1:
        sum += gradeList[i]

print(sum)

a,b=map(int,input().split())
print(a^b)