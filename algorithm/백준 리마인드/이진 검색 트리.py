import sys
sys.setrecursionlimit(10**9)

nums = []
while True:
    try:
        num = int(input())
        nums.append(num)

    except:
        break

def getMembers(numbers):
    if len(numbers) == 0:
        return []

    key = numbers[0]

    if len(numbers) == 2:
        return [numbers[1], key]

    elif len(numbers) == 1:
        return [key]

    else:
        leftSubTree = []
        rightSubTree = []

        for i in range(1, len(numbers)):
            target = numbers[i]
            if target < key:
                leftSubTree.append(target)
            else:
                rightSubTree.append(target)

        return getMembers(leftSubTree) + getMembers(rightSubTree) + [key]

answer = getMembers(nums)
for num in answer:
    print(num)