### the right most triangle pattern


def right_triangle(n):
    for i in range(n):
        for j  in range(i+1):
            print("*",end="")
        print("")
    return "pattern printed"

n=[3,5,10]
for x in n:
   print(right_triangle(x))