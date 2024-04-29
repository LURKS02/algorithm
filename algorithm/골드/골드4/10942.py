import sys
input = sys.stdin.readline

# 입력 처리
N = int(input().rstrip())  # 수열의 크기
numbers = list(map(int, input().rstrip().split()))  # 칠판에 적은 수
M = int(input().rstrip())  # 질문의 개수

# 팰린드롬 여부를 저장할 2차원 리스트 초기화
# dp[s][e]는 s번째 수부터 e번째 수까지의 부분 수열이 팰린드롬인지 여부를 저장
dp = [[0] * N for _ in range(N)]

# 길이가 1인 모든 부분 수열은 팰린드롬임
for i in range(N):
    dp[i][i] = 1

# 길이가 2인 부분 수열의 팰린드롬 여부를 확인
for i in range(N-1):
    if numbers[i] == numbers[i+1]:
        dp[i][i+1] = 1

# 길이가 3 이상인 부분 수열의 팰린드롬 여부를 동적 프로그래밍을 통해 계산
for length in range(3, N+1):  # 부분 수열의 길이
    for start in range(N-length+1):  # 시작 인덱스
        end = start + length - 1  # 끝 인덱스
        # 시작과 끝 수가 같고, 그 사이 부분 수열이 팰린드롬이면 현재 부분 수열도 팰린드롬
        if numbers[start] == numbers[end] and dp[start+1][end-1]:
            dp[start][end] = 1

# 질문에 대한 답변 출력
for _ in range(M):
    s, e = map(int, input().rstrip().split())
    print(dp[s-1][e-1])