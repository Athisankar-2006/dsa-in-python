### find the maximum consecutive once in an given array

## the input array should be 0 ,1

arr=[1,1,1,0,0,1,0,1,1,1,1,1]

def max_once(arr):

    max_count=0
    current_count=0
    for i in range(len(arr)):
        if arr[i]==1:
             current_count+=1
             max_count=max(max_count,current_count)
        else:
            current_count=0
    return max_count


print(max_once(arr))


