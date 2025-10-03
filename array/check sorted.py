arr=[11,43,48,51,61,86]

##1,check the array is ascending order

# def ascending(arr):
#       return all(arr[i]<=arr[i+1]
#       for i in range(len(arr)-1))
        
# print(ascending(arr))



# #2,descending order

# def descending(arr):
#     return all(arr[i]>=arr[i+1]  for i in range(len(arr)-1))

# print(descending(arr))



#,3 chcck both array is ascending or desending

def array1(arr):
    return arr==sorted(arr) or arr==sorted(arr,reverse=True)

print(array1(arr))


