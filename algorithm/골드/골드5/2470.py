def find_closest_to_zero(solutions):
    solutions.sort()
    left, right = 0, len(solutions) - 1
    closest = float('inf')
    answer = (0, 0)

    while left < right:
        mix = solutions[left] + solutions[right]
        if abs(mix) < closest:
            closest = abs(mix)
            answer = (solutions[left], solutions[right])

        if mix < 0:
            left += 1
        elif mix > 0:
            right -= 1
        else:
            return answer

    return answer

N = int(input())
l = list(map(int, input().split()))
print(*find_closest_to_zero(l))
