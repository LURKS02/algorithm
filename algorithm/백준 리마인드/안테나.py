N = int(input())
houses = list(map(int, input().split()))
houses.sort()
if len(houses) % 2 == 0:
    print(houses[len(houses) // 2 - 1])
else:
    print(houses[len(houses) // 2])