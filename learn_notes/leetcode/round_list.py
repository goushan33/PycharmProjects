def search(nums,target,low,high):
    '''
    我们发现循环数组存在一个性质：以数组中间点为分区，会将数组分成一个有序数组和一个循环有序数组。

如果首元素小于 mid，说明前半部分是有序的，后半部分是循环有序数组；
如果首元素大于 mid，说明后半部分是有序的，前半部分是循环有序的数组；
如果目标元素在有序数组范围中，使用二分查找；
如果目标元素在循环有序数组中，设定数组边界后，使用以上方法继续查找。
    '''

    mid = low + ((high - low)>>1)

    if nums[0] < nums[mid]:
        res = bserch(nums[:mid], target)
        if res:
            return res - 1
        else:
            return search(nums[mid:], target,mid,7)
    if nums[0] > nums[mid]:
        res = bserch(nums[mid + 1:], target)
        if res:
            return res - 1
        else:
            return search(nums[:mid+1],target,0,mid+1)

def bserch(arr, val):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if val < arr[mid]:
            high = mid - 1
        if val > arr[mid]:
            low = mid + 1
        if val == arr[mid]:
            return mid + 1
    return 0

nums=[4,5,6,7,0,1,2,3]
target=2
print(search(nums,target,0,7))