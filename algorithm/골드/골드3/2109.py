N = int(input())
lectures = []
day = [0] * (10000)

for _ in range(N):
    p, d = map(int, input().split())
    lectures.append((d, p))

lectures.sort(key=lambda x: (-x[1], x[0]))

for lecture in lectures:
    spot = lecture[0] - 1
    while spot >= 0:
        if day[spot] == 0:
            day[spot] = lecture[1]
            break
        spot -= 1

print(sum(day))
