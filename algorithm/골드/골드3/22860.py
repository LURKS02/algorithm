from collections import deque
import sys
input = sys.stdin.readline

# N = 폴더의 총 개수 (1,000)
# M = 파일의 총 개수 (1,000)
N, M = map(int, input().rstrip().split())

queryDictionary = dict()
folderDictionary = dict()
fileDictionary = dict()

for _ in range(N+M):
    P, F, C = input().split()
    if P in queryDictionary:
        queryDictionary[P].append((F, int(C)))
    if P not in queryDictionary:
        queryDictionary[P] = [(F, int(C))]

deq = deque(["main"])
while deq:
    key = deq.popleft()

    if key not in queryDictionary:
        continue

    for query in queryDictionary[key]:
        folderName, operation = query
        if operation == 1:
            if key not in folderDictionary:
                folderDictionary[key] = [folderName]
            else:
                folderDictionary[key].append(folderName)
            deq.append(folderName)

        elif operation == 0:
            if key not in fileDictionary:
                fileDictionary[key] = [folderName]
            else:
                fileDictionary[key].append(folderName)

# print(folderDictionary)
# print(fileDictionary)

# Q = 쿼리의 개수 (1,000)
Q = int(input())
for _ in range(Q):
    l = list(input().rstrip().split('/'))

    fileKey = l[-1]
    totalFileDictionary = dict()
    deq = deque([fileKey])

    while deq:
        key = deq.popleft()
        if key in fileDictionary:
            for file in fileDictionary[key]:
                if file in totalFileDictionary:
                    totalFileDictionary[file] += 1
                else:
                    totalFileDictionary[file] = 1

        if key in folderDictionary:
            for folder in folderDictionary[key]:
                deq.append(folder)

    print(len(totalFileDictionary.keys()), sum(totalFileDictionary.values()))
