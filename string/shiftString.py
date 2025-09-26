## check whether a string is a rotaton of another string


def check(s1,s2):
    
    if len(s1)!=len(s2):
        print("gimme the valid strings ")
        return False
    return s1 in (s1+s2)


s1="abcde"
s2="cdeab"
print(check(s1,s2))
