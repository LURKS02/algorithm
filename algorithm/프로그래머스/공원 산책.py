def solution(park, routes):
    dict = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
    x, y = -1, -1
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x, y = i, j

    for route in routes:
        direction, value = route.split()
        value = int(value)

        dx, dy = dict[direction]

        canMove = True
        for i in range(1, value+1):
            nx, ny = x + dx*i, y + dy*i
            # print(nx, ny)
            if nx < 0 or nx >= len(park) or ny < 0 or ny >= len(park[0]) or park[nx][ny] == 'X':
                canMove = False
                break

        if canMove:
            x, y = x + dx * value, y + dy * value

    answer = [x, y]
    return answer

print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))
