## find the number that appears once and other number twice

# ### counter method

# from collections import Counter
# def check_single_number(nums):
#     freq=Counter(nums)
#     for num ,count in freq.items():
#         if count==1:
#             return num
        

# nums=[2,2,1,1,5,7,7]
# print(check_single_number(nums))




# # brute force method

# def brute(nums):
#     for i in nums:
#         count=0
#         for j in nums:
#             if i == j:
#                 count+=1
#         if count==1:
#             return i
# nums=[2,2,1,1,5,7,7]
# print(brute(nums))
            


# using xor method

def xorMethod(nums):
     result=0
     for num in nums:
          result^=num
     return result
     
        
nums=[2,2,1,1,5,7,7]
print(xorMethod(nums))
            