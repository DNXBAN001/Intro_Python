# Name : Bandile Danxa
# Date : 18 May 2020
# Submission 6 - CupCake

decision = ""
print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')

response = input('Did anyone see you? (yes/no)\n').lower() #variable to store the user response

#decisions to be taken if someone see you
if response == 'no':
    response = input('Was it sticky? (yes/no)\n').lower()
    #decision to be taken based on whether it is sticky or not
    if response == 'no':
        response = input('Is it an Emausaurus? (yes/no)\n').lower()
        if response == 'no':
            response = input('Did the cat lick it? (yes/no)\n').lower()
            #decisions to be taken if the cat lick it or not
            if response == 'no':
                decision = 'Eat it.'
            else:
                response = input('Is your cat healthy? (yes/no)\n').lower()
                #decision to be taken based on the health of your cat
                if response == 'no':
                    decision = 'Your call.'
                else:
                    decision = 'Eat it.'
        else:
            response = input('Are you a Megalosaurus? (yes/no)\n').lower()
            #decision to be taken based on whether you are Megalsaurus or not
            if response == 'no':
                decision = "Don't eat it."
            else:
                decision = 'Eat it.'
    else:
        response = input('Is it a raw steak? (yes/no)\n').lower()
        #decision to be taken if it is raw steak or not,
        if response == 'no':
            r = input('Did the cat lick it? (yes/no)\n').lower()
            #decide based on whether the licked it or not
            if response == 'no':
                decision = 'Eat it.'
            else:
                response = input('Is your cat healthy? (yes/no)\n').lower()
                #if your cat is healthy then you can eat it, else dont eat it
                if response == 'no':
                    decision = 'Your call.'
                else:
                    decision = 'Eat it.'
        else:
            response = input('Are you a puma? (yes/no)\n').lower()
            #if it a raw steak and you are a puma the you can eat it, else dont eat it
            if response == 'no':
                decision = "Don't eat it."
            else:
                decision = 'Eat it.'

#decisions to be taken if no one see you
else:
    response = input('Was it a boss/lover/parent? (yes/no)\n').lower()
    #decisions to be taken if the person was a boss/lover/parent or not
    if response == 'no':
        decision = 'Eat it.'
    else:
        response = input('Was it expensive? (yes/no)\n').lower()
        #decisions to be taken depending on whether it is expensive or not
        if response == 'no':
            response = input('Is it chocolate? (yes/no)\n').lower()
            #decisions to be taken depending on whether it is chocolate or not
            if response == 'no':
                decision = "Don't eat it."
            else:
                decision = 'Eat it.'
        else:
            response = input('Can you cut off the part that touched the floor? (yes / no)\n').lower()
            if response == "no":
                decision = 'Your call.'
            else:
                decision = 'Eat it.'


print('Decision: ', decision)
