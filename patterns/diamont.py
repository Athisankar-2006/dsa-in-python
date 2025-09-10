### diament

def dia(n):
   for i in range(n):
        print(" "*(n-i) + "*"  * ((i*2)-1 ))

   for i in range(n):
       print(" "*(i) + "*"*(2*(n-i)-1))
   return "pattern printed"

print(dia(5))