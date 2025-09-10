### reverse the diamond pattern are hour glass pattern

def dia(n):
    for i in range(n):
        print(" "*i + "*"*(2*(n-i)-1))
    for i in range(1,n+1):
        print(" "*(n-i) + "*"*((2*i)-1))
    return "pattern printed"

print(dia(5))