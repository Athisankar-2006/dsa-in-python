## check whether two are anagram or not


## using sorted
'''
def check_anagram(s1,s2):
    s1=s1.replace(" "," ").lower()
    s2=s2.replace(" "," ").lower()
    return sorted(s1)==sorted(s2)

s1="bharath"
s2="bharath"
print(check_anagram(s1,s2))

'''

## using counter collections 

'''
from collections import Counter
def anagram(s1,s2):
       s1=s1.replace(" "," ").lower()
       s2=s2.replace(" "," ").lower()
       return Counter(s1)==Counter(s2)


s1="bharath"
s2="bharath"
print(anagram(s1,s2))


'''


## using manual frequency count

def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    freq={}
    for char in s1:
        freq[char]=freq.get(char,0)+1
    for char in s2:
        if char not in freq:
            return False
        freq[char]-=1
        if freq[char]<0:
            return False
    return True



s1="bharath"
s2="bharath"
print(anagram(s1,s2))


