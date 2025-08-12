### sort an array of 0's 1's and 2's

### counting sort approch

'''
def counting(arr):
    count=[0]*3
    for num in arr:
        count[num]+=1
        index=0
        for i in range(3):
             for _ in range(count[i]):
                  arr[index]=i
                  index +=1


arr=[1,2,2,1,0,1,1,2]
print(counting(arr))

'''


