import heapq


def solution(storey):
    stone = 0

    l = list(map(int, str(storey)))

    if len(l) == 1:
        if l[0] > 5:
            return 10 - l[0] + 1
        else:
            return l[0]

    else:
        for i in range(len(l) - 1, 0, -1):
            current = l[i]
            pre = l[i - 1]

            if current > 5:
                stone += 10 - l[i]
                l[i - 1] += 1
            elif current < 5:
                stone += l[i]
            else:
                if pre >= 5:
                    stone += 10 - l[i]
                    l[i - 1] += 1
                else:
                    stone += l[i]

        if l[0] > 5:
            stone += 10 - l[0] + 1
        else:
            stone += l[0]

        return (stone)


