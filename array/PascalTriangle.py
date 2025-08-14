#### pascal triangle

  
# ##1.simple interactive approach (using list)

# def pascal(n):
#     triangle=[]
#     for i in range(n):
#         row=[1]*(i+1)
#         for j in range(1,i):
#             row[j]=triangle[i-1][j-1]+triangle[i-1][j]
#             triangle.append(row)
#     return triangle

# n=5
# for row in pascal(n):
#     print(row)       
     
      


'''
##2.using combination formula 

import math
def pascal(n):
    for i in range(n):
        row=[math.comb(i,j) for j in range(i+1)]
        print(row)


n=5
print(pascal(n))


'''

#3, space -optimaized

def pascal_triangle(n):
    row=[1]
    for i in range(n):
        print(row)
        new_row=[1]
        for j in range(1,len(row)):
            new_row.append(row[j-1] + row[j])
            new_row.append(1)
            row=new_row

pascal_triangle(5)