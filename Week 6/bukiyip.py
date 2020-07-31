# Name : Bandile Danxa
# Date : 08 June 2020
# Submission 2 - Bukiyip



#This function is just for converting our list of characters back to string
def listToString(characterArray):
    text = ""
    for ele in characterArray:
        text += str(ele)
    return text

# This function converts a Bukiyip number (base-3) into a Decimal (base-10)
def bukiyip_to_decimal(bukiyipNumber):
    decimalNumber = 0
    i = 0
    tempVar = 0
    while (bukiyipNumber != 0):
        tempVar = bukiyipNumber % 10
        decimalNumber += tempVar * pow(3, i)
        bukiyipNumber = (bukiyipNumber // 10)         #take the bukiyip number and divide it to exclude the remainder
        i += 1
    return decimalNumber

def decimal_to_bukiyip(n):
    bukDigits = []
    bukiyipNumber = ''
    if n > 2:
        # divide with integral result (to discard remainder)
        decimal_to_bukiyip(n // 3)

    print(n % 3, end=' ')

# This function adds two bukiyip numbers
def bukiyip_add(a, b):
    result = bukiyip_to_decimal(a)+bukiyip_to_decimal(b)        #convert a and b into decimals to perform the arithmetic calculation
    # result = decimal_to_bukiyip(result)             #reverse the result which is in decimal form into bukiyip number
    # return result
    print()
    decimal_to_bukiyip(result)


# This function multiplies two bukiyip numbers
def bukiyip_multiply(a, b):
    result = bukiyip_to_decimal(a) * bukiyip_to_decimal(b)      #convert a and b into decimals to perform the arithmetic calculation
    # result = decimal_to_bukiyip(result)     #reverse the result which is in decimal form into bukiyip number
    # return result
    print()
    decimal_to_bukiyip(result)



# 1  = 001
# 2  = 002
# 3  = 010
# 4  = 011
# 5  = 012
# 6  = 020
# 7  = 021
# 8  = 022
# 9  = 100
# 10 = 101
# 11 = 102
# 12 = 110
# 13 = 111
# 14 = 112
# 15 = 120
# 16 = 121


# print(bukiyip_to_decimal(111)) #13
# decimal_to_bukiyip(12) #110
# bukiyip_add(11, 11) #22
# bukiyip_multiply(11, 11) #121