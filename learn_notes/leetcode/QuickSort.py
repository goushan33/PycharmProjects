def quick_sort(arr):
    if len(arr)<=1:
        return arr
    parti=partition(arr)
    return quick_sort(arr[:parti])+quick_sort(arr[parti:])
def partition(arr):
    pivot=arr[-1]
    i=0
    for j in range(len(arr)-1):
        if arr[j]<pivot:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[i],arr[-1]=arr[-1],arr[i]
    return i

array=[4,7,6,9,5,11,3,1,2]
print(quick_sort(array))

'''
快速排序：分而治之的思想
空间复杂度：O(1),在原地排序
时间复杂度：平均O(nlogn),最坏O(n2)
patition的思想：通过游标i把原始数组分成两部分，已处理+未处理。每次比较的是A[j]和pivot的值，直到j递增到末端。
'''
