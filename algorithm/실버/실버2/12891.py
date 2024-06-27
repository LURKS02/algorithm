S, P = map(int, input().split())
l = list(input())
nums = list(map(int, input().split()))

currentNums = [0] * 4
ans = 0

for i in range(P):
    if l[i] == 'A':
        currentNums[0] += 1
    if l[i] == 'C':
        currentNums[1] += 1
    if l[i] == 'G':
        currentNums[2] += 1
    if l[i] == 'T':
        currentNums[3] += 1

start = 0
end = P-1

while end < S:
    if currentNums[0] >= nums[0] and currentNums[1] >= nums[1] and currentNums[2] >= nums[2] and currentNums[3] >= nums[3]:
        ans += 1

    if end == S-1:
        break
    if l[start] == 'A':
        currentNums[0] -= 1
    if l[start] == 'C':
        currentNums[1] -= 1
    if l[start] == 'G':
        currentNums[2] -= 1
    if l[start] == 'T':
        currentNums[3] -= 1

    start += 1
    end += 1

    if l[end] == 'A':
        currentNums[0] += 1
    if l[end] == 'C':
        currentNums[1] += 1
    if l[end] == 'G':
        currentNums[2] += 1
    if l[end] == 'T':
        currentNums[3] += 1

print(ans)