N = int(input())

l = list(map(int, input().split()))

sc = sorted(set(l))

dict = {coord: idx for idx, coord in enumerate(sc)}

cc = [dict[i] for i in l]
print(*cc)