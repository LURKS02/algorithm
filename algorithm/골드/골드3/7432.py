import sys
input = sys.stdin.readline

N = int(input().rstrip())

dict = {}

def printDict(dict, depth = 0):
    keys = list(dict.keys())
    keys.sort()

    for key in keys:
        print(depth * " " + key)
        printDict(dict[key], depth + 1)

def inputDict(dict, s):
    if s not in dict:
        dict[s] = {}

for _ in range(N):
    inputs = input().rstrip().split('\\')
    dictCopy = dict

    for ip in inputs:
        inputDict(dictCopy, ip)
        dictCopy = dictCopy[ip]

printDict(dict)