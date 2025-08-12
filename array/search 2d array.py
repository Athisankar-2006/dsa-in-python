### search a key element in a two diamentional  array


matrix=[
    [6,3,8],
    [12,8,10],
    [32,2,6]
]

key=2


###  method 1 : brute force (in unsorted 2d array)  :

def search_2d(matrix,key):
    for i in matrix:
        for j  in i:
            if j==key:
                return True
    return False


print(search_2d(matrix,key))





'''


####  method:2  row and column wise sorted (matrix -elimination method)

def search_eliminates(arr,key):
    row,col=0,len(matrix[0])-1
    while row<len(matrix) and col>=0:
        if matrix[row][col]==key:
            return True
        elif matrix[row][col]>key:
            col-=1
        else:
            row+=1
    return False

print(search_eliminates(matrix,key))




'''