from datetime import datetime
while True:
    try:
        s=input()
        s1='2018-'+s+' 12:00:00'
        cday = datetime.strptime(s1, '%Y-%m%d %H:%M:%S')
        week=cday.strftime('%w')
        if week=='0':
            print('7')
        else:
            print(week)
    except:
        break