from collections import deque

S = input()

cnt = 0

A = deque()
B = deque()
C = deque()

for c in S:
    if c == 'A':
        A.appendleft(cnt)
    if c == 'B':
        B.appendleft(cnt)
    if c == 'C':
        C.appendleft(cnt)
    cnt += 1

# print(A)
# print(B)
# print(C)

result = 0
for c in A:
    if B and B[0] > c:
        B.popleft()
        result += 1
for c in B:
    if C and C[0] > c:
        C.popleft()
        result += 1

print(result)



