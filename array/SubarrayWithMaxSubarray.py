### print the subarray with maximum subarray (excented version of the max subarray sum)

def max_subarray(arr):
    max_sum=current_sum=0
    start=end=s=0
    for i in range(1,len(arr)):
        if( current_sum+arr[i] <arr[i] ):
           current_sum=arr[i]
           s=i
        else:
            current_sum+=arr[i]
            if current_sum>max_sum:
                max_sum=current_sum
                start=s
                end=i
    print("maximum subarray sum:",max_sum)
    print("subarray:",arr[start:end+1])


arr=[-2,-3,-1,4,2,1,-5,4]
max_subarray(arr)
           

