# Name : Bandile Danxa
# Date : 25 May 2020
# Submission 1 - Row
# The program prints a sequence of 7 numbers, starting from that value that is entered by the user


number = int(input("Enter a start number (between -6 and 93)\n"))

#if number entered is within constrait, print them in a row format
if number >= -6 and number <=93:
    for i in range(7):
        number = str(number).rjust(2) #right justify a number of field length 2
        # number = "{0:>2}".format(number)
        if i < 6:
            print(number, end =" ")
        else:
            print(number, end ="")
        number = int(number)+1

#if the number entered by the user is not within the expected constraint, print a warning message
else:
    print("The number entered must be between -6 and 93")