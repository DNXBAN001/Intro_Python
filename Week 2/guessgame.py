#Name : Bandile Danxa
#Date 11 May 2020
#submission 6
#This program prompts the user to guess the word and notifies them if they get it right or wrong

word = "Hydrogen".lower()   #variable to store the wod to be guessed
guessWord = ""              #variable to store user's guess
attemptsCount = 0           #variable to keep track of how many attempt the user took
status = False

while guessWord != word and attemptsCount < 3:
    guessWord = input("Enter your guess word : ").lower()
    if guessWord == word:
        print("Congratulations, your guess was correct!!")
        status = True
    else:
        print("Try again....")
        attemptsCount += 1
        status = False

if status :
    print("Great job!")
else:
    print("You have exhausted your guess attempts")
    print("The right word is : ", word)