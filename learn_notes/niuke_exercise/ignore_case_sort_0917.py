import re
while True:
    try:
        s = input()
        symbol = re.findall(r'[^0-9A-Za-z]', s)
        symbol_index = []
        for i in symbol:
            symbol_index.append(s.index(i))
            s = s.replace(i, '')

        res = [(x.lower(), x) for x in s]
        for i in range(len(res) - 1):
            for j in range(0, len(res) - 1 - i):
                if res[j][0] > res[j + 1][0]:
                    term = res[j]
                    res[j] = res[j + 1]
                    res[j + 1] = term
        r = []
        for i in range(len(res)):
            r.append(res[i][1])
        for i in range(len(symbol)):
            r.insert(symbol_index[i], symbol[i])
        R = ''
        for i in r:
            R += i
        print(R)
    except:
        break
