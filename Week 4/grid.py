# Name : Bandile Danxa
# Date : 25 May 2020
# Submission 3 - Grid
# This program prints numbers in a grid format

number = int(input("Enter the start number: "))
y = number

#if number entered is between -6 and 2, perform the instruction inside the if statements
if number > -6 and number < 2:
    for i in range(7): #for keeping track of
        for j in range(7):
            if number <= y+41:
                number = str(number).rjust(2)
                if j < 6:
                    print(number, end=" ")
                else:
                    print(number, end="")
                number = int(number) + 1
            else:
                break
        print() #skip to next line

else:
    print("The number entered is outside the boundary")