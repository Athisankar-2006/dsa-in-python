### merge two sorted array without using extra space

### naive approach sort+swap
'''
def merge_arr(arr1,arr2):
    n,m=len(arr1),len(arr2)
    for i in range(n):
        if arr1[i]>arr2[0]:
            arr1[i],arr2[0]=arr2[0],arr1[i]
            arr2.sort()
    return arr1,arr2

arr1=[2,4,9,5]
arr2=[1,3,7]

print(merge_arr(arr1,arr2))
'''

###gap method
def merge_arr(arr1,arr2):
    import math
    n,m=len(arr1),len(arr2)
    gap=math.ceil((n+m)/2)
    while gap>0:
        i,j=0,gap
        while j<n+m:
            if j<n and arr1[i]>arr1[j]:
                arr1[i],arr1[j]=arr1[j],arr1[i]
            elif j>=n and i<n and arr1[i]>arr2[j-n]:
                arr1[i],arr2[j-n]=arr2[j-n],arr1[i]
            elif j>=n and i>=n and arr2[i-n]>arr2[j-n]:
                arr2[i-n],arr2[j-n]=arr2[j-n],arr2[i-n]
            i+=1
            j+=1
        if gap==1:
            gap=0
        else:
            gap=math.ceil(gap/2)
        return arr1,arr2
    

    
arr1=[2,4,9,5]
arr2=[1,3,7]

print(merge_arr(arr1,arr2))

