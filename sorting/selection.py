

def selection(arr):
   n=len(arr)
   for i in range(n):
    minimum=i
    for j in range(i+1,n):
      if arr[j]<arr[minimum]:
        minimum=j
   arr[i],arr[minimum]=arr[minimum],arr[i]





arr=[12,4,27,15,28,12,42]
print("original array",arr)
selection(arr)
print("sorted array:",arr)