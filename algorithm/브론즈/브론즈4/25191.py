chicken = int(input())

cola, beer = map(int, input().split())
c = cola // 2
total = c + beer
print(min(chicken, total))