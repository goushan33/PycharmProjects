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
    return array

'''
时间复杂度O(n2)
空间复杂度：O(1)原地排序
稳定性：有
'''
array=[4,5,6,3,1,2]
print(insert_sort(array))

