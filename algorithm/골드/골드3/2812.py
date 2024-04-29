N, K = map(int, input().split())

number = input()

position = 0

while(K > 0):

    # print(position)
    firstNumber = int(number[position])

    noChange = True

    for i in range(position+1, len(number)):
        if firstNumber < int(number[i]) and K >= i - position:
            number = number[:position] + number[position+1:]
            K -= 1
            noChange = False
            break

    if noChange:
        position += 1
    # print(number)

print(number)

N, K = map(int, input().split())
number = input()

stack = []
remove_count = K

for num in number:
    while remove_count > 0 and stack and stack[-1] < num:
        stack.pop()
        remove_count -= 1
    stack.append(num)

# 만약 모든 숫자를 확인한 후에도 제거할 숫자가 남았다면, 끝에서부터 제거
result = ''.join(stack[:-remove_count]) if remove_count > 0 else ''.join(stack)

print(result)