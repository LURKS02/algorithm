import sys
input = sys.stdin.readline

n = int(input())
string = input().rstrip()
d = {}
answer = front = 0

for rear in range(len(string)):
    d.setdefault(string[rear], 0)
    d[string[rear]] += 1

    while len(d) > n:
        d[string[front]] -= 1
        if d[string[front]] == 0:
            del d[string[front]]

        front += 1
    answer = max(answer, rear-front+1)
print(answer)