import sys
input = sys.stdin.readline

def max_selected_applicants(applicants):
    applicants.sort(key=lambda x: x[0])

    max_interview_rank = float('inf')
    selected_count = 0

    for _, interview_rank in applicants:
        if interview_rank < max_interview_rank:
            selected_count += 1
            max_interview_rank = interview_rank

    return selected_count

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    applicants = [tuple(map(int, input().split())) for _ in range(N)]
    print(max_selected_applicants(applicants))