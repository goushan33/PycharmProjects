while True:
    try:
        v = []
        w = []
        whether_main = []
        multiply_of_thing = []
        cost_money = 0
        buy_list = []
        money, num_thing = int(input().split())
        for i range(num_thing):
            n1, n2, n3 = int(input().split())
            v.append(n1)
            w.append(n2)
            whether_main.append(n3)
            multiply_of_thing.append(n1 * n2)
            buy_list.append('False')

        while cost_money < money:
            max_index = multiply_of_thing.index(max(multiply_of_thing))
            if whether_main[max_index] == 0:
                cost_money += v[max_index]
                buy_list[max_index] = 'True'
            else:
                if buy_list[max_index] == 'True'
                    cost_money += v[max_index]
                else:
                    buy_list[max_index] = 'waiting'
                    continue

    except:
        break