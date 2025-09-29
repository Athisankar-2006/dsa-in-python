### is subsequence or not

##two pointer method
def subsequence(s1,s2):
    p1=0
    p2=0
    while(p1<len(s1) and p2<len(s2)):
        if s1[p1]==s2[p2]:
            p1+=1
            p2+=2
        else:
            p1+=1
    if p2==len(s2):
        return True
    return False

s1="abcde"
s2="bd"
print(subsequence(s1,s2))