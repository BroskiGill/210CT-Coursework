##Pseudocode
##  reverseString(s)
##  countWord<- COUNT s

##  IF countWord=0
##      RETURN ""
##  ELSE
##      RETURN reverseString s[1:] + s[0]+ " "
##userInput<-INPUT "Please enter words to be reversed: "
##PRINT reverseString(userInput.SPLIT(" "))



#This code will let a user input words that will be revered as an output
def reverseString(s):                                                       #1
    
    """ this function reverse strings"""

    countWord= len(s)                                                       #1

    if countWord ==0:                                                       #1
     #returns empty string 
        return str("")                                                      #1
    else:       
        #Takes the first letter and puts it in the end of the array#
        return reverseString(s[1:]) + str(s[0])+" "                         #1
userInput=input("Please enter words to be reversed: ")                      #1
#Splits each array
print(reverseString(userInput.split(" ")))                                  #1
# formula=6
#This means the Big O notation is O(1)
