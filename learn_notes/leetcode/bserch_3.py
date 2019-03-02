#变体三：查找第一个大于等于给定值的元素
def bserch(arr,val):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+((high-low)>>1)
        if val>arr[mid]:
            low=mid+1
        else:
            if mid==0:
                return mid
            elif val>arr[mid-1]:
                return mid
            else:
                high=mid-1
    return -1

arr=[1,2,3,4,5,5,5,6,7,8,9,10]
print(bserch(arr,9))


