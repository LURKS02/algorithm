import sys
input = sys.stdin.readline

N = int(input())
acids = list(map(int, input().split()))

leftIdx = 0
rightIdx = N-1

ans = abs(acids[leftIdx] + acids[rightIdx])
ansLeft = leftIdx
ansRight = rightIdx

while leftIdx < rightIdx:
    tmp = acids[leftIdx] + acids[rightIdx]

    if abs(tmp) < ans:
        ansLeft = leftIdx
        ansRight = rightIdx
        ans = abs(tmp)

        if ans == 0:
            break

    if tmp < 0:
        leftIdx += 1
    else:
        rightIdx -= 1

print(acids[ansLeft], acids[ansRight])