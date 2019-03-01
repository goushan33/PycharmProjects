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
            return array
'''
运用有序度的思想粗略计算平均时间复杂度O(n2)
空间复杂度O(1):原地排序
稳定性：有
'''
array=[4,5,6,3,1,2]
print(bubble_sort(array))