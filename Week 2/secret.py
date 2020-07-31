#Name : Bandile Danxa
#Date 12 May 2020
#submission 8
#program to guess the secret number

secret_number = 42  #create secret number
guess = 0 #variable to store user's guess

#as long as we have not found the secret number
while guess != secret_number:
    #get a new guess from user
    guess = eval(input("? "))
    #check if huess is too low
    if guess < secret_number:
        print("lo")
    #or too high
    elif guess > secret_number:
        print("hi")

print("Correct")    #print message indicating success