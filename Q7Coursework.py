import math
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
