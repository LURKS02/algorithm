friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]

def solution(friends, gifts):
    friendList = {}

    for friend in friends:
        friendList[friend] = {}

    for fromFriend in friends:
        for toFriend in friends:
            if fromFriend == toFriend:
                continue
            else:
                friendList[fromFriend][toFriend] = 0

    for gift in gifts:
        giftInfo = gift.split()
        fromPerson, toPerson = giftInfo[0], giftInfo[1]

        friendList[fromPerson][toPerson] += 1

    answerList = {}

    for friend in friends:
        answerList[friend] = 0

    for fromFriend in friends:
        for toFriend in friends:
            if fromFriend == toFriend:
                continue
            if friendList[fromFriend][toFriend] != friendList[toFriend][fromFriend]:

                if friendList[fromFriend][toFriend] > friendList[toFriend][fromFriend]:
                    answerList[fromFriend] += 1
                else:
                    answerList[toFriend] += 1

            elif friendList[fromFriend][toFriend] == friendList[toFriend][fromFriend]:
                fromFriendGain = 0
                for friend in friendList:
                    if friend == fromFriend:
                        continue
                    fromFriendGain += friendList[friend][fromFriend]
                fromFriendGive = 0
                for friend in friendList[fromFriend]:
                    fromFriendGive += friendList[fromFriend][friend]

                fromFriendIndex = fromFriendGive - fromFriendGain

                toFriendGain = 0
                for friend in friendList:
                    if friend == toFriend:
                        continue
                    toFriendGain += friendList[friend][toFriend]
                toFriendGive = 0
                for friend in friendList[toFriend]:
                    toFriendGive += friendList[toFriend][friend]

                toFriendIndex = toFriendGive - toFriendGain

                if fromFriendIndex > toFriendIndex:
                    answerList[fromFriend] += 1
                if fromFriendIndex < toFriendIndex:
                    answerList[toFriend] += 1

    return(max(answerList.values()) // 2)


print(solution(friends, gifts))