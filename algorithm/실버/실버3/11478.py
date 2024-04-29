import itertools

S = input()

dict = {}


for i in range(len(S)):
    for j in range(i, len(S)):
        newst = S[i:j + 1]
        if newst not in dict:
            dict[newst] = 1

print(sum(dict.values()))