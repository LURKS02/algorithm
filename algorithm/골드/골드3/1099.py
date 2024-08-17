from collections import defaultdict, Counter

word = input()
N = int(input())

wordDict = defaultdict(list)

for _ in range(N):
    w = input()
    wLen = len(w)
    wordDict[wLen].append(w)

dp = [float('inf')] * (len(word)+1)

dp[0] = 0

for i in range(1, len(word)+1):
    for key in wordDict.keys():
        if i >= key:
            tempWord = list(word[i-key: i])
            dataWords = wordDict[key]

            for d in dataWords:
                dList = list(d)
                if Counter(tempWord) != Counter(dList):
                    continue

                # print(i)
                # print(key)
                # print(tempWord)
                # print(dList)
                # print()
                count = 0
                for j in range(0, key):
                    if tempWord[j] != dList[j]:
                        count += 1

                dp[i] = min(dp[i], dp[i-key] + count)

if dp[len(word)] == float('inf'):
    print(-1)
else:
    print(dp[len(word)])
