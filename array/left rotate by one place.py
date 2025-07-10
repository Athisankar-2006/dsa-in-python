##left rotated an arry by one place

arr=[1,2,3,4,5]

##1,slicing method

# def left_rotate(arr):
#     return arr[1:]+arr[:1]

# print(left_rotate(arr))



###2,using (in-place method)

def left_rotate(arr):
    if not arr:
        return 0
    first=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[-1]=first
    return arr

print(left_rotate(arr))