### find union from the array

# def find_union(arr1,arr2):
#     return list(set(nums1) | set(nums2))

def find_union(arr1,arr2):
    result=[]
    for x in arr1:
        if x not in arr2:
            result.append(x)
    for x in arr2:
        if x not in arr1:
            result.append(x)
    return result


nums1=[1,2,3,4]
nums2=[4,5,6]
print(find_union(nums1,nums2))
