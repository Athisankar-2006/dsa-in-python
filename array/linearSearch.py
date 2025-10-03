### linear search 

def linear(nums,key):
    for i in nums:
        if nums[i]==key:
            return i
    return -1


nums=[1,2,3,4,5,6,7]
key=5
result=linear(nums,key)

if result!=True:
    print(f"Element {key} found at index {result}")
else:
    print("key not found")
