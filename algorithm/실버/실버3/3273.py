import sys

n = int(sys.stdin.readline().rstrip())
l = list(map(int, sys.stdin.readline().rstrip().split()))
x = int(sys.stdin.readline().rstrip())

l.sort()
start = 0
end = n - 1

count = 0
while(start < end):
    if l[start] + l[end] == x:
        count += 1
        start += 1
    elif l[start] + l[end] < x:
        start += 1
    elif l[start] + l[end] > x:
        end -= 1
print(count)