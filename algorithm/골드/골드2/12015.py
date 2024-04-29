import sys
import bisect

N = int(input())
l = map(int, input().split())

tails = []

for num in l:
    pos = bisect.bisect_left(tails, num)
    if pos < len(tails):
        tails[pos] = num
    else:
        tails.append(num)

print(len(tails))