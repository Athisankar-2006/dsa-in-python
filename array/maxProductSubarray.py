## maximum product subarray in an array

def max_product_subarry(nums):
    if not nums:
        return 0
    
    max_so_far=nums[0]
    min_so_far=nums[0]
    max_product=nums[0]

    for i in range(1,len(nums)):
        if nums[i]<0:                                           ###if negative swap min, max
            max_so_far,min_so_far=min_so_far,max_so_far
        max_so_far=max(nums[i],max_so_far*nums[i])
        min_so_far=min(nums[i],max_so_far*nums[i])
        max_product=max(max_product,max_so_far)

        return max_product



nums=[2,3,-2,4]
print(max_product_subarry(nums))