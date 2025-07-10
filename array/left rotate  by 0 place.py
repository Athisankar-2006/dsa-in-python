###left rotate  an array by  0 place


arr=[1,2,3,4,5,6]

#method 1
# def rotate_arr(arr,k):
#     n=len(arr)
#     if n==0 or k==0:
#         return arr
#     k=k%n
#     return arr[k:]+arr[:k]

# print(rotate_arr(arr,0))


#method 2 in place method


def rotate_inplace(arr,k):
    n=len(arr)
    if k==0 or n==0:
        return arr
    k=k%n
    reverse_arr(arr,0,k-1)
    reverse_arr(arr,k,n-1)
    reverse_arr(arr,0,n-1)
    return arr

def reverse_arr(arr,start,end):
    while start<end:
        arr[start],arr[end]  = arr[end],arr[start]
        start+=1
        end-=1

print(rotate_inplace(arr,3))



