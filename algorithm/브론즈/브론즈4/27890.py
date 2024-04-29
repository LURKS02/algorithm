x, N = map(int, input().split())

water = x
for i in range(N):
    if water % 2 == 0:
        water = (water//2)^6
    else:
        water = (2*water)^6

print(water)
