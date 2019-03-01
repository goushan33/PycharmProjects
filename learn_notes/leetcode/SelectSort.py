def select_sort(array):
    length=len(array)
    if length==1:
        return array
    for i in range(length-1):
        mini=i
        for j in range(i+1,length):
            if array[j]<array[mini]:
                mini=j
        array[i],array[mini]=array[mini],array[i]
    return array


'''
时间复杂度：n2
空间复杂度：1
稳定性：无
'''

array=[4,7,6,3,1,2]
print(select_sort(array))
