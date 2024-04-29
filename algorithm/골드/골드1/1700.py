N, K = map(int, input().split())

appliances = list(map(int, input().split()))

outlets = set()
plugOutCount = 0

for i in range(K):
    if appliances[i] in outlets:
        continue

    if len(outlets) < N:
        outlets.add(appliances[i])

    else:
        lastUse = -1
        for outlet in outlets:
            if outlet not in appliances[i:]:
                toRemove = outlet
                break
            else:
                nextUse = appliances[i:].index(outlet)
                if nextUse > lastUse:
                    lastUse = nextUse
                    toRemove = outlet
        outlets.remove(toRemove)
        outlets.add(appliances[i])
        plugOutCount += 1

print(plugOutCount)