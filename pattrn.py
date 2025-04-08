n = 10
nm = {}
def dimond (x):
     print(" " * ( n-x) , "*" *(2 *x -1))
     nm.update(x)
     


for x in range(n+1):
   dimond(x)
for y in range(n-1 ,0 ,-1):
   dimond(y)


print(nm)