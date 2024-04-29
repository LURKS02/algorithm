from collections import deque

puzzle = ""
for i in range(3):
    puzzle += "".join(list(input().split()))

visited = {puzzle: 0}
deq = deque([puzzle])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    while deq:
        puzzle = deq.popleft()
        cnt = visited[puzzle]
        z = puzzle.index('0')

        if puzzle == '123456780':
            return cnt

        x = z // 3
        y = z % 3

        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 3 and 0 <= ny < 3:
                nz = nx * 3 + ny
                puzzle_list = list(puzzle)
                puzzle_list[z], puzzle_list[nz] = puzzle_list[nz], puzzle_list[z]
                new_puzzle = "".join(puzzle_list)

                if visited.get(new_puzzle, 0) == 0:
                    visited[new_puzzle] = cnt
                    deq.append(new_puzzle)

    return -1

print(bfs())