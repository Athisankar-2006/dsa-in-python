### 4 sum method in brute force method

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

