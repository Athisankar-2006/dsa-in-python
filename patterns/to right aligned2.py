### right aligned to right aligned


def right_aligned(n):
    for i in range(n+1):
        print(" "*i+ "*"*(n-i))

    print("")
    return "pattern printed"

print(right_aligned(10))