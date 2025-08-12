## maximum sub array sum inm kadane's alogorithms

def kadanes(arr):
    max_sum=arr[0]
    current_sum=arr[0]
    for num in arr[1:]:
        current_sum=max(num,current_sum+num)
        max_sum=max(max_sum,current_sum)
    return max_sum

    
arr=[-2,-1,0,-2,-2,2,-1,0,1,2,0,1,1,1,2]
print(kadanes(arr))




##### brute force

'''

def brute(arr):
    max_sum=float('-inf')
    n=len(arr)
    for i in range(n):
        for j  in range(i,n):
            current_sum=0
            for k in range(i,j+1):
                current_sum +=arr[k]
                max_sum=max(max_sum,current_sum)   
    return max_sum


arr=[-2,-1,0,-2,-2,2,-1,0,1,2,0,1,1,1,2]
print(brute(arr))


'''