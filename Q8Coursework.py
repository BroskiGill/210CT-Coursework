
def removeVowels(word):
    vowels=["A","E","I","O","U","a","e","i","o","u"]
    if word=="":
        return removeVowels
    else:
        for i in word:
            if i in vowels:
                word=word.replace(i,"")
        return word

userInput=input("Please enter a word for which the vowels will be removed: ")
print(removeVowels(userInput))
                      
