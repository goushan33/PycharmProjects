#变体四：查找最后一个小于等于给定值的元素
def bserch(arr,val):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+((high-low)>>1)
        if arr[mid]>val:
            high=mid-1
        else:
            if mid==len(arr)-1:
                return mid
            elif arr[mid+1]>val:
                return mid
            else:
                low=mid+1
    return -1
arr=[1,2,3,4,5,5,5,6,7,8,9,10]
print(bserch(arr,5))
