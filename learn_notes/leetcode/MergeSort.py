def merge_sort(array):
    if len(array)<=1:
        return array
    q = len(array)//2
    left=merge_sort(array[:q])
    right=merge_sort(array[q:])
    return merge(left,right)

def merge(left,right):
    temp=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            temp.append(left[i])
            i+=1
        else:
            temp.append(right[j])
            j+=1
    #如果left\right 还有未放进去的元素
    temp+=left[i:]
    temp+=right[j:]
    #print(temp)
    return temp


array=[4,5,6,3,1,2]
print(merge_sort(array))
'''
时间复杂度：T(n)=2T(n/2)+n,后面的n 表示把两个有序数组合并为一个有序数组的时间复杂度为O(n).

空间复杂度：不是原地排序，O(n).这是相对于快排的一个弱点
稳定性：有
'''

