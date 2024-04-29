import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N, M = map(int, input().rstrip().split())
    people = []

    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        people.append((a, b))

    people.sort(key=lambda x: (x[1], x[0]))
    max_people = 0

    books = [False] * (N + 1)

    for a, b in people:
        for book in range(a, b + 1):
            if not books[book]:
                books[book] = True
                max_people += 1
                break

    print(max_people)