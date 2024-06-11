N = int(input())
wordList = [input() for _ in range(N)]
sortedWordList = sorted(list(enumerate(wordList)), key=lambda x: x[1])

def check(A, B):
    cnt = 0
    for i in range(min(len(A), len(B))):
        if A[i] == B[i]:
            cnt += 1
        else:
            break
    return cnt

length = [0] * (N+1)
maxLength = 0

for i in range(N-1):
    tmp = check(sortedWordList[i][1], sortedWordList[i+1][1])
    maxLength = max(maxLength, tmp)

    length[sortedWordList[i][0]] = max(length[sortedWordList[i][0]], tmp)
    length[sortedWordList[i+1][0]] = max(length[sortedWordList[i+1][0]], tmp)

first = 0
for i in range(N):
    if first == 0:
        if length[i] == max(length):
            first = wordList[i]
            print(first)
            pre = wordList[i][:maxLength]
    else:
        if length[i] == max(length) and wordList[i][:maxLength] == pre:
            print(wordList[i])
            break