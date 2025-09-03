###1. this is static pattern

def static_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print("")
    return "pattern printed"

print(static_pattern(5))
