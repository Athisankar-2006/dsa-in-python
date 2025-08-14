## three sum


'''     
## 1two pointer approch +sorting 

def three_sum(nums):
    nums.sort()
    res=[]
    n=len(nums)
    for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        l,r=i+1,n-1
        while(l<r):
            total=nums[i]+nums[l]+nums[r]
            if total<0:
                l+=1
            elif total>0:
                r-=1
            else:
                res.append([nums[i],nums[l],nums[r]])
                while l<r and nums[l]==nums[l+1]:
                    l+=1
                while l<r and nums[r]==nums[r-1]:
                    r-=1
                l+=1
                r-=1
    return res



print(three_sum())


'''
'''

##2 ,brute force 3 nested looop

def three_sum(nums):
    n=len(nums)
    res=set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k]==0:
                    res.add(tuple(sorted((nums[i],nums[j],nums[k]))))
    return list(res)


print(three_sum([-1,0,1,2,-1,-4]))


'''

##3 ,hash set \ hash map approach

def three_sum(nums):
    res=set()
    n=len(nums)
    for i in range(n):
        seen=set()
        for j in range(i+1,n):
            target=-nums[i]-nums[j]
            if target in seen:
                res.add(tuple(sorted((nums[i],nums[j],target))))
            seen.add(nums[j])

    return list(res)


print(three_sum([-1,0,1,2,-1,-4]))