#Pseudocode
## removeVowels(word)
## vowels<-["A","E","I","O","U","a","e","i","o","u"]
## IF word =""
##      return removeVowels
## ELSE
##   FOR i IN word 
##       IF i IN vowels
##           word<-word REPLACE("")
##   RETURN word
## userInput<-INPUT "Please enter a word for which the vowels will be removed: ")
## PRINT removeVowels(userInput)

def removeVowels(word):
    vowels=["A","E","I","O","U","a","e","i","o","u"]
    if word=="":
        return removeVowels
    else:
        #Checking each elements in word
        for i in word:
            #Checking each element in vowels
            if i in vowels:
                word=word.replace(i,"")
        return word

userInput=input("Please enter a word for which the vowels will be removed: ")
print(removeVowels(userInput))
                      
