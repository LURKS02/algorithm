N = int(input())
cards = list(map(int, input().split()))

minValue = float('inf')

for card in cards:
    val = 0
    tempCards = [card] * N

    for i in range(N):
        if cards[i] != tempCards[i]:
            val += 1

    minValue = min(minValue, val)

for i in range(N-1):
    for j in range(i+1, N):
        if (cards[j] - cards[i]) % (j-i) != 0:
            continue
        sub = (cards[j] - cards[i]) // (j-i)

        tempCards = [0] * N
        tempCards[i] = cards[i]

        for k in range(i, 0, -1):
            tempCards[k-1] = tempCards[k] - sub

        for k in range(i+1, N):
            tempCards[k] = tempCards[k-1] + sub

        val = 0

        for k in range(N):
            if cards[k] != tempCards[k]:
                val += 1

        minValue = min(minValue, val)

print(minValue)