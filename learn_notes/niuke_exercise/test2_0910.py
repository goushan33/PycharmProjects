while True:
    try:
        s = [1,10,81,0]
        for i in range(len(s) - 1):
            get_num = 0
            num_empty = s[i]
            while num_empty:
                if num_empty==2:
                    get_num+=1
                    num_empty=0
                if num_empty == 1:
                        num_empty = 0
                else:
                    get_num += num_empty // 3
                    num_empty = num_empty // 3 + num_empty % 3
            print(get_num)
    except:
        break