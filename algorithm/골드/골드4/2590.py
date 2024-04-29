paperList = [int(input()) for _ in range(6)]

ans = 0

existingOneZone = 0
existingTwoZone = 0

# 6칸 색종이
ans += paperList[5]

# 5칸 색종이
ans += paperList[4]
existingOneZone += paperList[4] * 11

# 4칸 색종이
ans += paperList[3]
existingTwoZone += paperList[3] * 5

# 3칸 색종이
plusValue = (paperList[2] - 1) // 4 + 1 if paperList[2] > 0 else 0
usedPaper = paperList[2] % 4
ans += plusValue

if usedPaper == 1:
    existingTwoZone += 5
    existingOneZone += 7
elif usedPaper == 2:
    existingTwoZone += 3
    existingOneZone += 6
elif usedPaper == 3:
    existingTwoZone += 1
    existingOneZone += 5

# 2칸 색종이
twoPaper = paperList[1] - existingTwoZone

if twoPaper > 0:
    existingTwoZone = 0
    ans += (twoPaper - 1) // 9 + 1
    usedPaper = twoPaper % 9

    if usedPaper != 0:
        existingOneZone += (9 - usedPaper) * 4

else:
    existingTwoZone -= paperList[1]

# 1칸 색종이
if existingTwoZone > 0:
    existingOneZone += existingTwoZone * 4

onePaper = paperList[0] - existingOneZone

if onePaper > 0:
    ans += (onePaper - 1) // 36 + 1

print(ans)
