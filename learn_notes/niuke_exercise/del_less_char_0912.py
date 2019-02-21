from collections import Counter

while True:
    try:
        s = input()
        c = Counter()
        key_r = []
        value_r = []
        res = ''
        for i in s:
            c[i] += 1
        for key, value in c.items():
            key_r.append(key)
            value_r.append(value)
        min_value = min(value_r)
        while min(value_r)<=min_value:
            term=min(value_r)
            ch=key_r[value_r.index(term)]
            s=s.replace(ch, '')
            key_r.pop(value_r.index(term))
            value_r.remove(term)
        print(s)

    except:
        break