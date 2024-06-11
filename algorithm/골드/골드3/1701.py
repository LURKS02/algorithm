s = input()
result = 0

def makeTable(pattern):
    length = len(pattern)
    table = [0] * len(pattern)
    j = 0

    for i in range(1, length):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

        # print(table)

    # print()
    return max(table)

for idx in range(len(s)):
    subStr = s[idx:]
    result = max(result, makeTable(subStr))

print(result)