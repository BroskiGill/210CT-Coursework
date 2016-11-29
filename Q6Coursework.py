#This code will let a user input words that will be revered as an output
def reverseString(s):
    
    """ this function reverse strings"""

    countWord= len(s)

    if countWord ==0:
     #returns back to the functions 
        return str("")
    else:
        return reverseString(s[1:]) + str(s[0])+" "
userInput=input("Please enter words to be reversed: ")
print(reverseString(userInput.split(" ")))
