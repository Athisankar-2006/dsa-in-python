### 4 sum method in brute force method



'''
def four_sum(arr,t):
    n=len(arr)
    res=set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if (arr[i]+arr[j]+arr[k]+arr[l]==t):
                        res.add(tuple(sorted([arr[i],arr[j],arr[k],arr[l]])))
                       
    return list(res)

arr=[1,4,3,5,6,7,2]
t=13

print(four_sum(arr,t))


'''

def fourSum(nums,target):
    nums.sort()
    n=len(nums)
    res=[]

    for i in range(n-3):
        if(i>0 and nums[i]==nums[i-1]):
            continue
        for j in range(n-2):
            if(j>i+1 and nums[j]==nums[j-1]):
                continue
            l,r=j+1,n-1
            while(l<r):
                total=nums[i]+nums[j]+nums[l]+nums[r]
                if(target==total):
                    res.append([nums[i],nums[j],nums[l],nums[r]])
                   
                    while(l<r and nums[l]==nums[l+1]):
                        l+=1
                    while (l<r and nums[r]==nums[r-1]):
                        r-=1
                    l+=1
                    r-=1
                    
                elif total<target:
                    l+=1
                else:
                    r-=1
    return res


      
         
         
   
   




# nums=[2,-3,-1,5,4]
# target=5
# print(fourSum(nums,target))

nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))
