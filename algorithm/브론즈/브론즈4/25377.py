N = int(input())
list = []

for i in range(N):
    a, b = map(int, input().split())
    if a <= b:
        list.append(b)

if len(list) == 0:
    print(-1)
else:
    print(min(list))