### right aligned pattern 

def pattern(n):
    m=(n*2)-1
    for i in  range(m):
        if (i>n):
            i=n*2-i
        for j in range(i):
            print("*",end="")

        print("")
    return "pattern printed"

print(pattern(5))
