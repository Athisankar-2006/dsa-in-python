# print the largest odd number from the string

## prefix based largest odd number (time complexity-0(n) ,space complexity-0(1))

def largest_odd_number(s: str) -> str:
    for i in range(len(s)-1, -1, -1):
        if int(s[i]) % 2 == 1:
            return s[:i+1]
    return ""

s=['346252']

print(largest_odd_number(s))


