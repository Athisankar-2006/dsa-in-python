####pyramid

def ptn(n):
    for  i in range(n+1):
        print(" "*(n-i) + "*"*((i*2)-1))
    print("")
    return "pattern printed"


print(ptn(5))