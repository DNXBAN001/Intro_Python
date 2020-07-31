#Name : Bandile Danxa
#Date 11 May 2020
#submission 7
#The program creates/implements the exponent function

def power(baseNumber, index):
    result = 1
    for i in range(index):
        result *= baseNumber
    return result


print(power(5, 3)) #call the power function and print the exponent