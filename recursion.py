inputdata = int(input('enter a number :- '))
def factorial (n):
    if n < 2 :
        return 1
    else :
        return n  * (factorial(n-1))
    
fact = factorial(inputdata)

print(fact)
