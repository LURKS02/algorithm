N = int(input())
inputString = input()

num = N // 2

if N % 2 == 0:
    firstText = inputString[:num]
    secondText = inputString[num:]
else :
    firstText = inputString[:num]
    secondText = inputString[num + 1:]

sum = 0
for i in range(num):
    if firstText[-(i + 1)] != secondText[i]:
        sum += 1

print(sum)