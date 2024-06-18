# N = 교실의 크기 (20)
N = int(input())
numberOfStudents = N * N

# 인덱스: 학생 번호, 값: 선호하는 학생 번호 리스트
studentPreferences = [set() for _ in range(numberOfStudents)]
students = []

for i in range(numberOfStudents):
    l = list(map(int, input().split()))
    studentPreferences[l[0]-1] = set([n - 1 for n in l[1:]])
    students.append(l[0]-1)

NON = -1

studentMap = [[NON] * N for _ in range(N)]
emptyMap = [[NON] * N for _ in range(N)]
favoriteMap = [[set() for _ in range(N)] for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(N):
        e = 0
        for k in range(4):
            ni, nj = i + dx[k], j + dy[k]
            if 0 <= ni < N and 0 <= nj < N:
                e += 1
        emptyMap[i][j] = e

for student in students:
    favoriteSet = studentPreferences[student]

    seatX, seatY = -1, -1

    # 1. 좋아하는 학생이 가장 많이 인접한 칸
    favoriteSeats = []
    favoriteNumber = -1

    for i in range(N):
        for j in range(N):
            if studentMap[i][j] != NON:
                continue
            fn = len(favoriteMap[i][j] & favoriteSet)

            if fn > favoriteNumber:
                favoriteNumber = fn
                favoriteSeats = [(i, j)]
            elif fn == favoriteNumber:
                favoriteSeats.append((i, j))

    if len(favoriteSeats) == 1:
        seatX, seatY = favoriteSeats[0][0], favoriteSeats[0][1]

    # 2. 인접한 칸 중에서 비어있는 칸이 가장 많은 칸
    else:
        possibleSeats = set(favoriteSeats)
        emptySeats = []
        emptyNumber = -1

        for i in range(N):
            for j in range(N):
                if (i, j) not in favoriteSeats:
                    continue
                if emptyMap[i][j] > emptyNumber:
                    emptyNumber = emptyMap[i][j]
                    emptySeats = [(i, j)]
                elif emptyMap[i][j] == emptyNumber:
                    emptySeats.append((i, j))

        seatX, seatY = emptySeats[0][0], emptySeats[0][1]

    studentMap[seatX][seatY] = student

    for i in range(4):
        nx, ny = seatX + dx[i], seatY + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            emptyMap[nx][ny] -= 1
            favoriteMap[nx][ny].add(student)

    # print("studentMap")
    # for i in range(N):
    #     print(*studentMap[i])
    # print("emptyMap")
    # for i in range(N):
    #     print(*emptyMap[i])
    # print("favoriteMap")
    # for i in range(N):
    #     print(*favoriteMap[i])
    # print()


ans = 0
for i in range(N):
    for j in range(N):
        student = studentMap[i][j]
        studentFavoriteList = studentPreferences[student]
        studentNeighbors = favoriteMap[i][j]

        favoriteScore = len(studentFavoriteList & studentNeighbors)

        if favoriteScore == 0:
            ans += 0
        elif favoriteScore == 1:
            ans += 1
        elif favoriteScore == 2:
            ans += 10
        elif favoriteScore == 3:
            ans += 100
        elif favoriteScore == 4:
            ans += 1000

print(ans)
