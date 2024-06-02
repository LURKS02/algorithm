import sys
input = sys.stdin.readline

village = []
totalPeople = 0

N = int(input())

for i in range(N):
    distance, people = map(int, input().split())
    village.append((distance, people))
    totalPeople += people

village.sort(key=lambda x: x[0])

count = 0

for i in range(N):
    count += village[i][1]
    if count >= totalPeople/2:
        print(village[i][0])
        break


