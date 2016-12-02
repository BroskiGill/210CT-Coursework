import math
##Pseudocode
## pn(n)
## checkPrimeNumber(x,y)
##      IF y<=1
##         RETURN n," is a prime number"
##      ELSE IF x mod y=0
##         RETURN n,"is not a prime number"
##      ELSE
##         RETURN checkPrimeNumber(x,y-10
##    RETURN  checkPrimeNumber(n,round(SquareRoot(n))
##
## UserInput<- INPUT "Enter a number to check whether it is a prime number: "
## Print pn(userInput)
def pn(n):
    def checkPrimeNumber(x,y):
        if (y<=1):
            return (str(n)+" is a prime number")
        elif (x % y==0):
            return (str(n)+" is not a prime number")
        else:
            return checkPrimeNumber(x,y-1)
    return checkPrimeNumber(n,round(math.sqrt(n)))

userInput=int(input("Enter a number to check whether it is a prime number: "))
print(pn(userInput))
