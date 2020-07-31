# Submission 2
# Date : 15 June 2020

# Dictionary to store response keyword and their respective entries
keywordResponses = {"crashed" : "Are the drivers up to date",
                    "blue" : "Ah, the blue screen of death. And then what happened?",
                    "hacked": "You should consider installing anti-virus software.",
                    "bluetooth": "Have you tried mouthwash?",
                    "windows": "Ah, I think I see your problem. What version?",
                    "apple": "You do mean the computer kind?",
                    "spam": "You should see if your mail client can filter messages.",
                    "connection": "Contact Telkom"}

#This fnction check if the keyword entered matches any of the entries in the dictionary
def isKeywordMatch(keyword):
    for i in keywordResponses:
        if keyword == i:
            return True
    return False

def main():

    problem = input('Welcome to the automated technical support.\nPlease describe your problem:\n')
    keyword = problem.lower()
    while True:
        if isKeywordMatch(keyword):     #check if the keyword matches any of the entries
            print(keywordResponses[keyword])
        elif keyword == 'quit':         #check if the user entered 'quit' and if that is true then break out of the loop
            break
        else:                           #else meaning if the user input/keyoword does not match ny of the entries in the
            print('Curious, tell me more.')
        keyword = input().lower()

#main function called
main()