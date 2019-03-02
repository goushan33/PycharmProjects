'''
粗略比较冒泡排序以及插入排序的执行效率
'''
import random,time

a = [[random.randint(1, 21) for j in range(1, 100)] for i in range(1, 11)]
def bubble_sort(array):
    length=len(array)
    for i in range(length):
        flag = False#每次冒泡遍历记录有无数据交换
        for j in range(length-1-i):
            if array[j]>array[j+1]:
                term=array[j]
                array[j]=array[j+1]
                array[j+1]=term
                flag=True
        if flag==False:
            break

def insert_sort(array):
    length=len(array)
    if length==1:
        return array
    for i in range(1,length):
        value=array[i]#无序段的第一个元素
        j=i-1
        while j>=0:
            if array[j]>value:
                array[j+1]=array[j]
            else:
                break
            j-=1
        array[j+1]=value



if __name__=="__main__":
    start = time.clock()
    for arr in a:
        bubble_sort(arr)
    end = time.clock()
    print("bubble: ", end - start)

    start2 = time.clock()
    for arr in a:
        insert_sort(arr)
    end2 = time.clock()
    print("insert: ", end2 - start2)


