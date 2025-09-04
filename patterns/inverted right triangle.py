#### i dont know this name of this pattern


def right_triangle(n):
    for i in range(n+1):
        for j in range(n-(i-1)):
            print("*",end="")
        print("")

    return "pattern printed"



def right_triangle2(n):
    for i in range(n+1):
        for j in range(n-(i-1)):
            print(i,end="")
            i+=1
        print("")

    return "pattern printed"


print(right_triangle(5))
print(right_triangle2(5))