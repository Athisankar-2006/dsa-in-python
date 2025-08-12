####  find the leader element in an array
matrix=[1,5,6,8,4,3,2]


'''
## best approch right to left traversal

def leader(matrix):
    n=len(matrix)
    leaders=[]
    matrix_from_right=matrix[-1]
    leaders.append(matrix_from_right)

    for i in range(n-2,-1,-1):
        if matrix[i]>matrix_from_right:
            matrix_from_right=matrix[i]
            leaders.append(matrix_from_right)
    return leaders[::-1]
   

print(leader(matrix))


'''


#### brute force approch
def brute(matrix):
    n=len(matrix)
    leader=[]
    for i in range(n):
        is_leader=True
        for j in range(i+1,n):
            if matrix[i]<=matrix[j]:
                is_leader=False
                break
        if is_leader:
            leader.append(matrix[i])
    return leader

print(brute(matrix))