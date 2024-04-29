def explode_string(string, bomb):
    stack = []
    bomb_length = len(bomb)

    for char in string:
        stack.append(char)
        # 스택의 길이가 폭발 문자열의 길이 이상일 때만 검사
        if len(stack) >= bomb_length:
            # 스택의 끝부분이 폭발 문자열과 일치하는지 확인
            if ''.join(stack[-bomb_length:]) == bomb:
                # 폭발 문자열과 일치하면 스택에서 해당 문자들을 제거
                del stack[-bomb_length:]

    # 스택에 남은 문자들을 합쳐 최종 결과 문자열 생성
    result = ''.join(stack)

    # 결과 문자열이 비어있으면 "FRULA" 출력, 그렇지 않으면 결과 문자열 출력
    return result if result else "FRULA"


# 입력 받기
string = input().strip()
bomb = input().strip()

# 함수 호출 및 출력
print(explode_string(string, bomb))