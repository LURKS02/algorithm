A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if A < 0:
    time = -A*C + D + E*B
elif A == 0:
    time = D + E+B
else:
    time = E*(B-A)

print(time)