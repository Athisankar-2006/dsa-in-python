
arr=[1,32,43,5,7]


# method:1
# print(max(arr))



# method:2
# arr.sort()
# print(arr[-1])



# method:3
# print(sorted(arr)[-1])


#method:4 =>using for loop
largest=arr[0]
for i in arr:
    if i>largest:
        largest=i
print(largest)


