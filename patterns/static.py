###1. this is static pattern

def static_pattern(n):
    for i in range(n):
        for j in range(n):
            print(j+1,end="")
        print("")
    return "pattern printed"

def static_pattern2(n):
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print("")
    return "pattern printed"


n=[5]
for x in n:
   print(static_pattern(x))
   print(static_pattern2(x))


