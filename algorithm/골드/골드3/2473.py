def sol(solutions):
    solutions.sort()
    length = len(solutions)
    closest_sum = float('inf')
    answer = []

    for i in range(length):
        left, right = i + 1, length - 1

        while left < right:
            current_sum = solutions[i] + solutions[left] + solutions[right]

            if abs(current_sum) < abs(closest_sum):
                closest_sum = current_sum
                answer = [solutions[i], solutions[left], solutions[right]]

            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                return answer

    return answer

N = int(input())
l = list(map(int, input().split()))

print(*sol(l))