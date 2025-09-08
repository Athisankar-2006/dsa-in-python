### reverse pyramid

def rp(n):
    for  i in range(1,n+1):
        print(" "*i + '*' * (2 * (n - i) - 1))

    print("")
    return "pattern printed"


print(rp(7))
