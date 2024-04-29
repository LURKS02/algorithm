N, K = map(int, input().split())

l = []
for i in range(1, N + 1):
    l.append(i)

index = 0

print('<', end ='')
while(len(l) > 0):
    index = (index + (K - 1)) % len(l)
    print(l.pop(index), end='')

    if len(l) != 0:
        print(', ', end='')
print('>', end='')