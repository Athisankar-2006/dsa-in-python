## reverses the strings characters

## two pointer approach
'''

def rev(s):
    l=0
    r=len(s)-1
    while (l<r):
        s[l],s[r]=s[r],s[l]
        l+=1
        r-=1
    return s


'''


def rev(s):
    stack=[]
    for i in s:
        stack.append(i)
    i=0
    while(len(stack) > 0):
        l= stack.pop()
        s[i]=l
        i+=1
    return s
    



s=["h","e","l","l","o","w"]
print(rev(s))