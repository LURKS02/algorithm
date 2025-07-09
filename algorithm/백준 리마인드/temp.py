import sys

input = sys.stdin.readline
L = int(input())                                    # 기관총 진지 앞쪽의 길이
ML, MK = map(int, input().split())                  # 기관총의 유효 사거리 ML, 기관총의 1m당 살상력 MK
C = int(input())                                    # 수평 세열 지향성 지뢰의 개수
zombies = [0] + [int(input()) for _ in range(L)]    # 좀비s


def solution(C):

    attack = [0] # 누적합

    for idx in range(1, L+1):
        ml = max(0, idx - ML)
        damage = attack[idx-1] - attack[ml]

        if zombies[idx] <= damage + MK:
            attack.append(attack[idx-1] + MK)
        else:
            if C > 0 :
                C -= 1
                attack.append(attack[idx-1])
            else:
                return "NO"

    return "YES"


print(solution(C))