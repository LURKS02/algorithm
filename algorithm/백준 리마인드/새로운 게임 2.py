from collections import defaultdict, deque

N, K = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

horses = dict()
board = defaultdict(deque)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(K):
    x, y, d = map(int, input().split())
    horses[i] = (x-1, y-1, d-1)
    board[(x-1, y-1)].append(i)

def changeDirection(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    else:
        return 2

for turn in range(1000):
    for i in range(K):
        px, py, pd = horses[i]

        nx, ny = px + dx[pd], py + dy[pd]

        if 0 <= nx < N and 0 <= ny < N:
            # 흰색
            if matrix[nx][ny] == 0:
                pushFlag = False

                remained = deque()

                while board[(px, py)]:
                    member = board[(px, py)].popleft()
                    if member == i:
                        pushFlag = True
                    if pushFlag:
                        board[(nx, ny)].append(member)
                        prevD = horses[member][2]
                        horses[member] = (nx, ny, prevD)

                        if len(board[(nx, ny)]) >= 4:
                            print(turn+1)
                            exit(0)
                    else:
                        remained.append(member)

                board[(px, py)] = remained

            # 빨강
            elif matrix[nx][ny] == 1:
                pushFlag = True

                remained = deque()

                while board[(px, py)]:
                    member = board[(px, py)].pop()

                    if pushFlag:
                        board[(nx, ny)].append(member)
                        prevD = horses[member][2]
                        horses[member] = (nx, ny, prevD)

                        if len(board[(nx, ny)]) >= 4:
                            print(turn+1)
                            exit(0)
                    else:
                        remained.appendleft(member)
                    if member == i:
                        pushFlag = False

                board[(px, py)] = remained

            # 파랑
            else:
                nd = changeDirection(pd)

                nnx, nny = px + dx[nd], py + dy[nd]

                if nnx < 0 or nnx >= N or nny < 0 or nny >= N:
                    horses[i] = (px, py, nd)
                elif matrix[nnx][nny] == 2:
                    horses[i] = (px, py, nd)
                elif matrix[nnx][nny] == 0:
                    pushFlag = False

                    remained = deque()

                    while board[(px, py)]:
                        member = board[(px, py)].popleft()
                        if member == i:
                            pushFlag = True
                        if pushFlag:
                            board[(nnx, nny)].append(member)
                            if member != i:
                                prevD = horses[member][2]
                                horses[member] = (nnx, nny, prevD)
                            else:
                                horses[member] = (nnx, nny, nd)

                            if len(board[(nnx, nny)]) >= 4:
                                print(turn + 1)
                                exit(0)
                        else:
                            remained.append(member)

                    board[(px, py)] = remained

                else:
                    pushFlag = True

                    remained = deque()

                    while board[(px, py)]:
                        member = board[(px, py)].pop()

                        if pushFlag:
                            board[(nnx, nny)].append(member)

                            if member != i:
                                prevD = horses[member][2]
                                horses[member] = (nnx, nny, prevD)
                            else:
                                horses[member] = (nnx, nny, nd)

                            if len(board[(nnx, nny)]) >= 4:
                                print(turn + 1)
                                exit(0)
                        else:
                            remained.appendleft(member)
                        if member == i:
                            pushFlag = False

                    board[(px, py)] = remained

        else:
            nd = changeDirection(pd)

            nnx, nny = px + dx[nd], py + dy[nd]

            if nnx < 0 or nnx >= N or nny < 0 or nny >= N:
                horses[i] = (px, py, nd)
            elif matrix[nnx][nny] == 2:
                horses[i] = (px, py, nd)
            elif matrix[nnx][nny] == 0:
                pushFlag = False

                remained = deque()

                while board[(px, py)]:
                    member = board[(px, py)].popleft()
                    if member == i:
                        pushFlag = True
                    if pushFlag:
                        board[(nnx, nny)].append(member)
                        if member != i:
                            prevD = horses[member][2]
                            horses[member] = (nnx, nny, prevD)
                        else:
                            horses[member] = (nnx, nny, nd)

                        if len(board[(nnx, nny)]) >= 4:
                            print(turn + 1)
                            exit(0)
                    else:
                        remained.append(member)

                board[(px, py)] = remained

            else:
                pushFlag = True

                remained = deque()

                while board[(px, py)]:
                    member = board[(px, py)].pop()

                    if pushFlag:
                        board[(nnx, nny)].append(member)

                        if member != i:
                            prevD = horses[member][2]
                            horses[member] = (nnx, nny, prevD)
                        else:
                            horses[member] = (nnx, nny, nd)

                        if len(board[(nnx, nny)]) >= 4:
                            print(turn + 1)
                            exit(0)
                    else:
                        remained.appendleft(member)
                    if member == i:
                        pushFlag = False

                board[(px, py)] = remained

print(-1)
