import math

l = list(map(int, input().split()))

ans = 99999999

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        for k in range(j + 1, len(l)):
            mo = abs(l[i] * l[j]) // math.gcd(l[i], l[j])
            myo = abs(l[k] * mo) // math.gcd(l[k], mo)
            if ans > myo:
                ans = myo

print(ans)