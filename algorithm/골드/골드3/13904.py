N = int(input())
works = []
day = [0] * (1000)

for _ in range(N):
    d, w = map(int, input().rstrip().split())
    works.append((d, w))

works.sort(key=lambda x: (-x[1], x[0]))

# print(works)

for work in works:
     spot = work[0] - 1
     while spot >= 0:
         if day[spot] == 0:
             day[spot] = work[1]
             break
         spot -= 1

print(sum(day))