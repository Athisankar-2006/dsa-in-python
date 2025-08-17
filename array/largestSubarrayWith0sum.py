## largest subarray with given sum


##1,brute force

'''

def largest_sum(arr):
    n=len(arr)
    max_len=0
    for i in range(n):
        curr_sum=0
        for j in range(i,n):
            curr_sum+=arr[j]
            if curr_sum==0:
                max_len=max(max_len,j-i+1)
    return max_len

arr=[-1,1,4,5,-5,-4]
print(largest_sum(arr))

'''

##2,hashing with prefix sum


def largest_sum(arr):
    prefix_sum=0
    max_len=0
    seen={}
    for i,num in enumerate(arr):
        prefix_sum +=num
        if prefix_sum==0:
            max_len=i+1
        if prefix_sum in seen:
            max_len=max(max_len,i-seen[prefix_sum])
        else:
            seen[prefix_sum]=i
    return max_len


arr=[-1,1,4,5,-5,-4]
print(largest_sum(arr))