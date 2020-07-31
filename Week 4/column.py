# Name : Bandile Danxa
# Date : 25 May 2020
# Submission 2 - Column
# The program prints out every 7th number in the range n to n+41 on the next line in a column form

x = ""
number = int(input("Enter a number between -6 and 2\n"))
y = number

#if number entered is within the constraints, print the numbers in column format
if number >= -6 and number <= 2:
    for i in range(number+41):

        #if number is within the range n + 41 then continue printing the numbers
        if number <= y + 41:
            #x = "{0:>2}".format(number)
            x = str(number).rjust(2)
            print(x)
            #number = int(number)+7
            number = int(number) + 7

        #else break out of the loop
        else:
            break

else:
    print("The number entered must be between -6 and 2")
