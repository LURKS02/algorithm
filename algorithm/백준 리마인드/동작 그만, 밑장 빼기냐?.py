N = int(input())
cards = list(map(int, input().split()))

m = []
my = [0]
next = [0]

for i in range(N):
    if i % 2 == 0:
        m.append(cards[i])
        my.append(my[-1] + cards[i])
    else:
        next.append(next[-1] + cards[i])

maxValue = 0

# 밑장빼기를 안하는 경우
maxValue = max(maxValue, my[-1])

# 자신의 차례에 밑장 빼기를 하는 경우
for i in range(N):
    if i % 2 == 0:
        idx = i // 2
        maxValue = max(maxValue, my[idx] + cards[-1] + next[-2] - next[idx])

# 상대의 차례에 밑장 빼기를 하는 경우
for i in range(N):
    if i % 2 == 1:
        idx = (i + 1) // 2
        maxValue = max(maxValue, my[idx] + next[-2] - next[idx-1])

print(maxValue)