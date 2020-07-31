# Bandile Danxa
# Submission 1
# Date : 22 June 2020


# This function is filtering out all the words to be ignored and update the value of the title
def filterWordsNotToIgnore(title, wordsToIgnore):
    for i in title:
        for j in wordsToIgnore:
            if i == j:
                title.remove(i)

wordsToIgnore = list(input("Enter words to be ignored separated by commas: ").upper().split(', ')) ##get words to ignore and convert everything to uppercases

title = list(input("Enter a title to generate its acronym: \n").upper().split(' ')) #get title and convert everything to uppercases

filterWordsNotToIgnore(title, wordsToIgnore)    # update value of title list, removing all the words to be ignored

acronym = ""    #initially our acronym value will be none

for ele in title:           # go through each element in the title list
    acronym += ele[0]       # append all the first letters of each word in the title list

print("\nThe acronym is: ", acronym) # print out the resulting acronym