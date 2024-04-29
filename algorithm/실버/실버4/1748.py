N = input()

l = len(N)

sum = 0
for i in range(1, l):
    sum += (pow(10, i) - pow(10, i-1)) * i
ex = (int(N) - pow(10, l-1) + 1) * l
print(sum + ex)