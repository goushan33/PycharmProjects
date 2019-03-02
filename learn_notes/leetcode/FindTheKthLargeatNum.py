#O(n)时间复杂度内求解无须数组内第k大元素
def k_largest_num(arr,k):
    if len(arr)==1 and k==1:
        return arr[0]
    i=partition(arr)
    if k==(i+1):
        return arr[i]
    if k>i+1:
        return k_largest_num(arr[i+1:],k-i-1)
    if k<i+1:
        return k_largest_num(arr[:i],k)

def partition(arr):#要将大元素放在前面
    pivot=arr[-1]
    i=0
    for j in range(len(arr)-1):
        if arr[j]>pivot:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[i],arr[-1]=arr[-1],arr[i]
    return i


array=[4,7,6,9,5,10,8,3,1,2]
print(k_largest_num(array,4))