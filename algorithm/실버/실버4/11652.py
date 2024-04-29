import sys
N = int(sys.stdin.readline().strip())

dict = {}

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1

maxcount = max(dict.values())
l = [k for k,v in dict.items() if v == maxcount]
print(min(l))