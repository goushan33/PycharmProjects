#二分查找
'''
三个容易出错的地方：循环退出条件、mid 的取值，low 和high 的更新.
适用场景：
1、数据有序，数据底层必须放在数据，链表是不行的，因为需要随机访问
2、对于小规模的数据，顺序遍历查找和二分查找并不会有太大差别
3、二分查找更适合处理静态数据，也就是没有频繁的删除、插入操作

'''
def bserch(arr,val):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+(high-low)//2#mid=(low+high)//2为啥不这么写，因为当low,high很大时容易溢出
        if val==arr[mid]:
            return mid
        elif val >arr[mid]:
            low=mid+1
            '''low=mid,high=mid,为啥不这么写，
            因为当low=high=3时，如果arr[3]不等于查找的那个值，
            此时，mid=low=high,再次更新low,high，low和hign的值未变
            那么就永远无法退出循环
            '''
        else:
            high=mid-1