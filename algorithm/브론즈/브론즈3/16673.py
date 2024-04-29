C, K, P = map(int, input().split())

def collect(C, K, P):
    return K * C + P * pow(C, 2)

sum = 0
for i in range(C):
    sum += collect(i+1, K, P)

print(sum)