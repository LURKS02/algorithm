inputNum = int(input())

sum = 0


def checkNum(num):
    global sum

    if num // 10 == 0:
        print(sum)
    else:
        mylist = []
        mynum = num
        while (mynum > 0):
            mylist.append(mynum % 10)
            mynum = mynum // 10

        newNum = 1
        for num in mylist:
            newNum *= num

        sum += 1
        checkNum(newNum)


checkNum(inputNum)