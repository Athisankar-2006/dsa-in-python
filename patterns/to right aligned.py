#### pattern


def ptn(n):
    for i in range(1,n+1):
          print(" "*(n-i) + "*"*i)
    print("")
    return "pattern printed"
       

n=5
print(ptn(n))
