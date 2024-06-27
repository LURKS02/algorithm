import sys
input = sys.stdin.readline

N, B, W = map(int, input().split())
stone = input().rstrip()

left = 0
WCount = 0
BCount = 0
maxLen = 0

for right in range(N):
    if stone[right] == 'W':
        WCount += 1
    else:
        BCount += 1

    while BCount > B:
        if stone[left] == 'W':
            WCount -= 1
        else:
            BCount -= 1
        left += 1
    if WCount >= W:
        maxLen = max(maxLen, right-left+1)
print(maxLen)