import bisect

N = int(input())

cups = list(map(int, input().split()))

cups.sort()

ans = float('inf')
ansList = []

for i in range(0, len(cups)-2):
    firstCup = cups[i]
    for j in range(i+1, len(cups)-1):
        secondCup = cups[j]
        cupSums = firstCup + secondCup
        targetCup = -cupSums

        idx = bisect.bisect_left(cups, targetCup)

        if abs(cupSums + cups[idx-1]) < abs(ans) and i != idx-1 and j != idx-1:
            ans = cupSums + cups[idx-1]
            ansList = [cups[i], cups[j], cups[idx-1]]
        if idx != len(cups):
            if abs(cupSums + cups[idx]) < abs(ans) and i != idx and j != idx:
                ans = cupSums + cups[idx]
                ansList = [cups[i], cups[j], cups[idx]]

print(*sorted(ansList))
