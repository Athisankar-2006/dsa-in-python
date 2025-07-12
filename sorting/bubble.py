
def bubble(arr):
    len1=len(arr)
    for i in range(len1):
        for j in range(0,len1-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]




arr=[12,1,23,21,56,32]

print("before bubble sort:",arr)

bubble(arr)
print("After the bubble sort:",arr)




# n=input("Enter the array element:")
# arr=[]

# for i in range(n):
#     element= int(input(f"Enter element:{i+1}:"))
#     arr.append(element)

# print(arr)