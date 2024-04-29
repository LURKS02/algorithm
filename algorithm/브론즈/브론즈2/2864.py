A, B = input().split()

maxA = A.replace('5', '6')
maxB = B.replace('5', '6')

minA = A.replace('6', '5')
minB = B.replace('6', '5')

print(int(minA) + int(minB))
print(int(maxA) + int(maxB))