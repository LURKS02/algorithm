def solution(players, callings):
    playerDictionary = {}

    for i in range(len(players)):
        playerDictionary[players[i]] = i

    for calling in callings:
        index = playerDictionary[calling]
        tempPlayer = players[index-1]
        players[index-1] = calling
        players[index] = tempPlayer

        playerDictionary[calling] = index-1
        playerDictionary[tempPlayer] = index

    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))