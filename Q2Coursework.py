def factorial_trailing_zero(array):
    """ This function returns the trailing
        number of zeros of a factorial number"""

    multiple = 1
    five=0

    for i in range(array):
        multiple=multiple*(i+1)

        for j in range(2,array+1):

            while j>0:
                if j %5==0:
                    five= five+1
                    j=j/5
                else:
                    break
        return five

userInput=int(input("Please enter a number which will return the trailing number of zeros of a factorial: "))
print(factorial_trailing_zero(userInput))
