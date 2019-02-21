#用队列list实现约瑟夫环
def yuesefuhuan(nums,call):
    peoples=[]
    for i in range(nums):
        peoples.append(True)

    result = []
    num=1
#用双重循环模拟 ‘循环链表’，不是真正的循环链表。
    while(any(peoples)):
        for index,person in enumerate(peoples):
            if person:#跳过之前已经被标记为false的
                if num == call:
                    peoples[index] = False
                    result.append(index + 1)
                    num = 1
                else:
                    num += 1

    print(result)

yuesefuhuan(20,3)

