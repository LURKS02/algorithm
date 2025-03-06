def solution(m, musicinfos):
    # 우선 입력 m에 대해서 어떤 문자로 되어 있는지 파싱을 해서 저장을 해야 한다.

    # 그리고 각 musicinfos에 대해서 재생 시간을 파싱한다.
    # 파싱한 재생 시간으로 전체 문자열을 구하고, 인덱스로 ?
    # 그리고 이걸 정답과 비교한다. 인덱스로
    # 이렇게 되면 문자열 최대 길이가 24 * 60 = 1440 인데
    # 1440 * 1439 번 비교?? -> 1500 * 1500 = 2250000
    # 이걸 100번 비교하면 225000000... 시간 초과??

    # 입력 문자열 파싱
    idx = 0
    inputArr = []

    while idx < len(m):
        if m[idx] == '#':
            temp = inputArr.pop()
            inputArr.append(temp + '#')
        else:
            inputArr.append(m[idx])
        idx += 1

    # 노래를 발견하기 위한 조건
    timePlay = 0
    answer = ''

    # 각 musicinfos 순회
    for line in musicinfos:
        # 파싱
        commands = line.split(",")
        startTimeCommand = commands[0]
        endTimeCommand = commands[1]
        title = commands[2]
        originSong = commands[3]

        # 노래 파싱
        sidx = 0
        song = []

        while sidx < len(originSong):
            if originSong[sidx] == '#':
                temp = song.pop()
                song.append(temp + '#')
            else:
                song.append(originSong[sidx])
            sidx += 1

        # 시간 파싱, 저장
        startTime = 0
        endTime = 0
        startParsed = list(map(int, startTimeCommand.split(":")))
        startTime = startParsed[0] * 60 + startParsed[1]
        endParsed = list(map(int, endTimeCommand.split(":")))
        endTime = endParsed[0] * 60 + endParsed[1]

        timeInterval = endTime - startTime

        # timeInterval 동안 순회를 돌아야 함.
        # 한정된 배열 song을 순회하면서 입력 문자열과 동일한지 판단해야 함.
        idx = 0
        visitedIdx = set()
        finishFlag = False

        while idx < timeInterval:
            if finishFlag: break

            realIdx = idx % len(song)
            if realIdx in visitedIdx:
                idx += 1
                continue

            visitedIdx.add(realIdx)
            songIdx = 0
            targetIdx = realIdx

            for _ in range(len(m)):
                if inputArr[songIdx] == song[targetIdx]:
                    songIdx += 1

                    if songIdx == len(inputArr):
                        if timeInterval > timePlay:
                            timePlay = timeInterval
                            answer = title
                        finishFlag = True
                        break
                else:
                    songIdx = 0

                targetIdx += 1
                targetIdx = targetIdx % len(song)

            idx += 1

    if answer == '':
        return '(None)'
    else:
        return answer

print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))