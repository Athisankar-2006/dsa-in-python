
arr=[12,34,54,32,23]

# method:1
# arr.sort()
# print(arr[-2])


# method:2
# print(sorted(arr)[-2])

first=second=float('-inf')
for i in arr:
    if i>first:
        second=first
        first=i
    elif first>i>second:
        second=i
print("second largest:",second)