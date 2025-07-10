### move zero to the end in an array

arr=[1,0,6,0,34,5,0]

###  mehtod 1:  two pointer approch
'''

def  move_zero(arr):
    n=len(arr)
    non_zero_index=0
    for i in range(n):
        if arr[i]!=0:
            arr[non_zero_index],arr[i]=arr[i],arr[non_zero_index]
            non_zero_index+=1
    return arr
        

print(move_zero(arr))

'''


### method 2: brute  force method

'''
def brute_force(arr):
    result=[]
    for num in arr:
        if num!=0:
            result.append(num)
    ####add 0
    return result+[0]*(len(arr)-len(result))

print(brute_force(arr))

'''

###method 3: list comprehension

def move_zero(arr):
    non_zero=[num for num in arr if num!=0]
    zero=[0]*(len(arr)-len(non_zero))
    return non_zero+zero


print(move_zero(arr))