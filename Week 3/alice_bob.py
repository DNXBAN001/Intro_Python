# Name : Bandile Danxa
# Date : 18 May 2020
# Submission 5 - Alice_Bob
#This program compares the scores of alice and bob (read from user) and prints out their points based on the scores

def compareTriplets(a, b):
    alice = list(map(int, a.split()))
    bob = list(map(int, b.split()))
    alicePoints = 0
    bobPoints = 0

    #check if the values typed by the user are within the constraints 1-100 inclusive
    for x in alice:
        if not(x > 1 and x <= 100): #if values in alice list are not within the range do not perform comparison
            return "The value(s) in the alice list is/are not within the costraints" #else return an error message
    for y in bob:  #if values in alice list are not within the range do not perform comparison
        if not(y > 1 and y <= 100):
            return "The value(s) in the bob list is/are not within the costraints"  # else return an error message

    #otherwise perform the comparison
    for i in range(3):
        if (alice[i] > bob[i]):
            alicePoints += 1
        elif (alice[i] < bob[i]):
            bobPoints += 1

    return [alicePoints, bobPoints] #return their scores

alice = input("Enter Alice's triplets : ")
bob = input("Enter Bob's triplets : ")

print(compareTriplets(alice, bob))