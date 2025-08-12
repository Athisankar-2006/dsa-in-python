
### 2 sum in two pointer  appproch

# arr=[1,2,3,4,5,6]
'''

def twosum():
    t=10
    l=0
    r=len(arr)-1
    h=1
    while(l<r):
        act=arr[l]+arr[r]
        if (act==t):
            h=0
            print(l,r)
            break
        elif (act<t):
            l=l+1
        elif(act>t):
            r=r-1
    if h==1:
        print("no combination")



twosum()

'''

### two pointer in brust force

def brust_force(arr,t):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i]+arr[j]==t):
                print(arr[i],arr[j])
    return []

arr=[1,2,3,4,5,6] 
t=10
brust_force(arr,t)




