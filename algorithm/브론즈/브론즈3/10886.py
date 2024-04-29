N = int(input())

A = 0
B = 0
for i in range(N):
    ans = int(input())
    if ans == 0:
        A += 1
    else:
        B += 1

if A > B:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')