N, M = map(int, input().split())

helmets = list(map(int, input().split()))
armors = list(map(int, input().split()))

maxH = max(helmets)
maxA = max(armors)

print(maxH + maxA)