from collections import deque

def solution(numbers, hand):
    answer = ''

    numberList = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]

    left = (3, 0)
    right = (3, 2)

    def bfs(start, end):
        x, y = start

        deq = deque([(x, y, 0)])
        visited = [[False] * 3 for _ in range(4)]
        visited[x][y] = True

        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        while deq:
            curX, curY, count = deq.popleft()

            if matrix[curX][curY] == end:
                return count

            for i in range(4):
                nx = curX + dx[i]
                ny = curY + dy[i]

                if 0 <= nx < 4 and 0 <= ny < 3 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    deq.append((nx, ny, count+1))

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = numberList[number]

        elif number in [3, 6, 9]:
            answer += 'R'
            right = numberList[number]

        else:
            leftCost = bfs(left, number)
            rightCost = bfs(right, number)

            if leftCost < rightCost:
                answer += 'L'
                left = numberList[number]

            elif leftCost > rightCost:
                answer += 'R'
                right = numberList[number]

            else:
                if hand == 'left':
                    answer += 'L'
                    left = numberList[number]
                else:
                    answer += 'R'
                    right = numberList[number]

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))