res=[None]*8
def eightQueen(row):
    if row==8:
        print(res)
        return 0
    for col in range(8):#每一行都有八种放置方法
        if isOK(row,col):
            res[row]=col
            eightQueen(row+1)

#判断第row 行放置在col列可不可以
def isOK(row,col):
    leftCol=col-1
    rightCol=col+1
    i=row-1
    while i>=0:#往上逐行考察
        if res[i]==col:#在coL这一列有没有放置元素;
            return False
        if leftCol>=0:#考察左上对角线
            if res[i]==leftCol:
                return False
        if rightCol<8:
            if res[i]==rightCol:
                return False
        i-=1
        leftCol-=1
        rightCol+=1
    return True
'''
def printQueen(res):
    for i in range(8):
        for j in range(8):
            if res[i]==j:
                print('Q ')
            else:
                print('* ')
        print('\n')
    print('\n')
'''
eightQueen(0)