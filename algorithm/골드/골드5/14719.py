H, W = map(int, input().split())
walls = list(map(int, input().split()))

ans = 0
for i in range(1, W-1):
    leftMax = max(walls[:i])
    rightMax = max(walls[i+1:])

    compare = min(leftMax, rightMax)

    if walls[i] < compare:
        ans += compare - walls[i]

print(ans)