N = int(input())
player = list(map(int, input().split()))

def findMaxIndex(player):
    pIndex = -1
    maxValue = -1

    for i in range(len(player)):
        if player[i] > maxValue:
            maxValue = player[i]
            pIndex = i

    return pIndex

k = 0
ans = 0
while k < N-1:
    maxIndex = findMaxIndex(player)

    if maxIndex == 0:
        if player[maxIndex] > player[maxIndex + 1]:
            ans += player[maxIndex] - player[maxIndex + 1]
            player.pop(maxIndex)
        else:
            ans += player[maxIndex + 1] - player[maxIndex]
            player.pop(maxIndex + 1)

    elif maxIndex == len(player) - 1:
        if player[maxIndex] > player[maxIndex - 1]:
            ans += player[maxIndex] - player[maxIndex - 1]
            player.pop(maxIndex)
        else:
            ans += player[maxIndex - 1] - player[maxIndex]
            player.pop(maxIndex-1)

    else:
        previousIndex = maxIndex - 1
        nextIndex = maxIndex + 1

        if abs(player[maxIndex] - player[previousIndex]) < abs(player[maxIndex] - player[nextIndex]):
            if player[maxIndex] > player[previousIndex]:
                ans += player[maxIndex] - player[previousIndex]
                player.pop(maxIndex)
            else:
                ans += player[previousIndex] - player[maxIndex]
                player.pop(previousIndex)
        elif abs(player[maxIndex] - player[nextIndex]) < abs(player[maxIndex] - player[previousIndex]):
            if player[maxIndex] > player[nextIndex]:
                ans += player[maxIndex] - player[nextIndex]
                player.pop(maxIndex)
            else:
                ans += player[nextIndex] - player[maxIndex]
                player.pop(nextIndex)

    k += 1

print(ans)