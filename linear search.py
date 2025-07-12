##linear search

##method 1:
arr=[1,2,3,4,5,6,7,8]
key =5


# def linear(arr,key):
#     for i in range(len(arr)):
#         if arr[i]==key:
#             print(f"{key}:key was found")
#             return f"{i}th index"
#     return 

# print(linear(arr,key))



###method 2: enumerate

def linear(arr,target):
    for index,value in enumerate(arr):
        if value==target:
            return index
    return False

print(linear(arr,key))
    