# Submission 1
# Date : 15 June 2020

import random

responses =["Have you tried it on a different operating system?",
            "Did you reboot it?", "What colour is it?",
            "You should consider installing anti-virus software.",
            "Contact Telkom.", "I should get that looked at if I were you."]

def main():

    problem = input('Welcome to the automated technical support system. Please describe your problem:\n')
    color = input('What colour is it?\n')
    while True:
        #print(random.choice(responses))
        print(responses[random.randint(0, 5)])
        reply = input()
        if reply == 'quit':
            break

if __name__=='__main__': main()