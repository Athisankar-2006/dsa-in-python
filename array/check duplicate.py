### check the duplicate from the sorted array

arr=[1,1,2,2,3,3,4,5,5,5,7]



# #1,two pointer approch

# def duplicate(arr):
#     if not arr:
#         return 0
#     j=0
#     for i in range(1,len(arr)):
#         if arr[i]!=arr[j]:
#             j+=1
#             arr[j]=arr[i]
#     return  arr[:j+1]

# print(duplicate(arr))



#2, brute force approch

def duplicate(arr):
    if not arr:
        return 0
    unique=[arr[0]]
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            unique.append(arr[i])
    return unique

print(duplicate(arr))



###3, using set() method
# def remove_duplicate(arr):
#     return sorted(set(arr))

# print(remove_duplicate(arr))