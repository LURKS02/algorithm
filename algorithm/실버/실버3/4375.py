while True:
    try:
        n = int(input())
        start = '1'
        while (True):
            if int(start) % n == 0:
                print(len(start))
                break
            else:
                start += '1'

    except:
        break
