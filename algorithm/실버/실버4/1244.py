import sys

switchNumber = int(sys.stdin.readline().rstrip())
switches = list(map(int, sys.stdin.readline().rstrip().split()))
N = int(sys.stdin.readline().rstrip())

def toggle(n):
    if n == 0:
        return 1
    else:
        return 0

def maleSwitch(switch):
    for i in range(1, len(switches) + 1):
        if i % switch == 0:
            switches[i - 1] = toggle(switches[i-1])
def femaleSwitch(switch):
    start = switch - 1
    end = switch - 1
    while(start >= 0 and end < len(switches)):
        if start == end:
            switches[start] = toggle(switches[start])
            start -= 1
            end += 1
        elif switches[start] == switches[end]:
            switches[start] = toggle(switches[start])
            switches[end] = toggle(switches[end])
            start -= 1
            end += 1
        else:
            break

for _ in range(N):
    sex, switch = map(int, input().split())
    if sex == 1:
        maleSwitch(switch)
    else:
        femaleSwitch(switch)

for index, s in enumerate(switches):
    print(s, end=' ')
    if (index + 1) % 20 == 0:
        print()