while True:
    try:
        stopword = ''
        str = []
        for line in iter(input, stopword):
            str.append(line)
        print(str)

    except:
        break