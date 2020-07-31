#Name : Bandile Danxa
#Date 11 May 2020
#submission 5
#This program performs 5 basic arithmetic operations based on the user choice


print("Enter your first number : ")
firstNum = float(input()) #get first number from user
print("Enter the operation you want to perform : ")
arithOperation = input() #get the arithmetic operation
print("Enter your second number : ")
secNum = float(input()) #get second number from user
result = 0

#decide which operation to perform based on user inputs
if arithOperation == '+':
    result = firstNum+secNum
    print(firstNum ," + " ,secNum ," = " ,result)
elif arithOperation == '-':
    result = firstNum - secNum
    print(firstNum ," - " ,secNum ," = " ,result)
elif arithOperation == '*':
    result = firstNum*secNum
    print(firstNum ," * " ,secNum ," = " ,result)
elif arithOperation == '/':
    if secNum == 0 :
        print("Division by zero cannot be performed...")
    else :
        result = firstNum/secNum
        print(firstNum ," / " ,secNum ," = " ,result)
elif arithOperation == '%':
    result = firstNum%secNum
    print(firstNum," % ", secNum, " = ", result)
else :
    print("The operation you entered is invalid...try again")