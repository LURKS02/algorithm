N = input()
listedN = list(N)
length = len(N)

path = set()

def tracking(start, end, str, pathString):
    if str == N and pathString not in path:
        path.add(pathString)

    if start > 0:
        newStart = start - 1
        newChar = listedN[newStart]
        newStr = newChar + str
        newPathString = pathString + newStr
        tracking(newStart, end, newStr, newPathString)

    if end < length-1:
        newEnd = end + 1
        newChar = listedN[newEnd]
        newStr = str + newChar
        newPathString = pathString + newStr
        tracking(start, newEnd, newStr, newPathString)

for i in range(length):
    tracking(i, i, listedN[i], listedN[i])
print(len(path))