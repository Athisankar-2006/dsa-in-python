## nested paranthesise

def parentheses(s:str)->int:
    if not s:
        return 0
    p=0
    result=0
    for i in s:
        if i=='(':
            p+=1
            result=max(result,p)
        elif i==')':
            p-=1
    return result
s="lj9(ah(2=49)(sd)(jsb))"
print(parentheses(s))