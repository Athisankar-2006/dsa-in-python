###find the missing element in an given  array

arr=[0,1,2,4,5]



##method 1:  using sum formula (best approch)

def find_missing(arr):
    n=len(arr)
    exp_sum= n*(n+1) // 2
    actual_sum=sum(arr)
    return exp_sum - actual_sum

print(find_missing(arr))




'''
###method :2 using xor [bit manipulation]

def find_missing(arr):
    n=len(arr)
    xor1=0
    xor2=0
    for i in range (n):
        xor1 ^=arr[i]
        xor2 ^=i
    xor2=n
    return xor1 ^ xor2


print(find_missing(arr))


'''