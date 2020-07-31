# Name : Bandile Danxa
# Date : 08 June 2020
# Submission 3 - Piglatin
# This program translates a text from english to pig latin and from pig latin back to english

#   These are conditions for translating from english to piglatin
#   1. if the word begins with a vowel, ‘way’ should be appended (example: ‘apple’ becomes ‘appleway’)
#   2. if the word begins with a sequence of consonants, this sequence should be moved to the
#   end, prefixed with ‘a’ and followed by ‘ay’ (example: ‘please’ becomes ‘easeaplay’)

#This function checks if the text begins wth a vowel or not and returns a boolean
def beginsWithVowel(text):
    for ele in "AEIOUaeiou":
        if text[0] == ele:
            return True
    return False

def beginsWithConsonant(text):
    for ele in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
        if text[0] == ele:
            return True
    return False

#This function checks if a character is a consonant or not and returns a boolean
def isConsonant(character):
    for el in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
        if character == el:
            return True
    return False

#This function checks if a character is a vowel or not and returns a boolean
def isVowel(character):
    for ele in "AEIOUaeiou":
        if character == ele:
            return True
    return False

#This function is just for converting our list of characters back to string
def listToString(characterArray):
    text = ""
    for ele in characterArray:
        text += str(ele)
    return text

#converts string to a list of characters
def stringToArray(text):
    charArr = []
    for i in text:
        charArr.append(i)
    return charArr


# This function returns the Pig Latin sentence for a given English sentence.
def to_pig_latin(englishText):
    text = englishText.split()      # split the english sentence into a list of words
    txt = ''
    for pos in range(len(text)):    # go through each word in the list of english words
        currentWord = text[pos]
        if beginsWithVowel(currentWord):    # if the current english word begins with a vowel
            currentWord += "way"            # then add "way" at the end of english text

        elif beginsWithConsonant(currentWord):       # if it begins with a sequence of consonants
            currentWord = stringToArray(currentWord) # convert my current word into a list of characters
            currentWord.append('a')                  # first append 'a' at the end of the list of the currentWord

            # traverse through the entire current word
            for i in range(len(currentWord)):
                if isConsonant(currentWord[0]):               # if the first character of current is a consonant
                    currentWord.append(currentWord[0])        # then put it at the end of the text
                    currentWord = currentWord[1:]           # update value of our text
            currentWord.append('ay')                   # and then finally add 'ay' at the end
        text[pos] = listToString(currentWord)
        txt += text[pos]+" "        # store the series of words in a sentence

    return txt

# This function returns the English sentence for a given Pig Latin sentence.
def to_english(piglatinText):
    piglatinWordsArray = piglatinText.split()   # split the piglatin sentence/text into a words list
    txt = ''
    tempText = []
    tempChar = []
    englishSentence = ''
    for word in piglatinWordsArray:
        if word[-3:] == 'way':      # if the word ends with 'way'
            txt = word[:-3]         # hen remove the 'way' at the end to restore the word back to english

        elif word[-2:] == 'ay':     # if the word ends with 'ay'
            txt = word[:-2]         # remove the 'ay'
            while txt[-1]!= 'a':
                if isConsonant(txt[-1]):                        # check if the last term is consonant
                    tempText = stringToArray(txt[:-1])          # if it is consonant remove it at the end
                    tempChar = stringToArray(txt[-1])           # store last character on tempChar variable
                    tempChar.append(listToString(tempText))     # append the new text on tempChar list
                    tempText = tempChar                         # the last character will be at the beginning of the new text
                    txt = listToString(tempText)                # store the value of the new text on txt variable
            if txt[-1] == 'a':
                    txt =txt[:-1]

        englishSentence += txt + ' '        # update the value of english sentence

    return englishSentence




# #main program starts here
# choice = input("(E)nglish or (P)ig Latin?\n").upper()
# if choice == 'E':
#     sentence = input("Enter an english sentence:\n")
#     print("\nPig-Latin : ", toPiglatin(sentence))
# 
# elif choice == 'P':
#     sentence = input("Enter a Pig Latin sentence:\n")
#     print("\nEnglish : ", toEnglish(sentence))
# 
# else:
#     print("\nChoose E or P")



