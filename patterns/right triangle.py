### the right most triangle pattern


def right_triangle(n):
    for i in range(n):
        for j  in range(i+1):
            print("*",end="")
        print("")
    return "pattern printed"



def right_triangle2(n):
    for i in range(n):
        for j  in range(i+1):
            print(j+1,end="")
        print("")
    return "pattern printed"

def right_triangle3(n):
    for i in range(1,n+1):
        val=1 if i % 2 != 0 else 0
        for j in range(1,i+1):
            print(val,end="")
            val=1-val
        print("")
        
    return "pattern printed"




n=[3,5,10]
for x in n:
    print(right_triangle(x))
    print(right_triangle2(x))
    print(right_triangle3(x))