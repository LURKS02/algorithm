N = int(input())

sum = 0
doubleSum = 0
tripleSum = 0
for i in range(N):
    sum += (i + 1)
    tripleSum += pow(i+1, 3)

doubleSum += pow(sum, 2)

print(sum)
print(doubleSum)
print(tripleSum)