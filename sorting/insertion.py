def  insertion(arr,n):
    for i in range(n-1):
        j=i
        while (j>0 and j<j-1):
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j=j-1







arr=[1,42,23,53,64,63]
print("before sorting:",arr)
n=len(arr)
insertion(arr,n)
print("after sorting:",arr)