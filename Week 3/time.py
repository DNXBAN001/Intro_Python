# Name : Bandile Danxa
# Date : 18 May 2020
# Submission 2 - Time

hours = eval(input("Enter the hours: "))
minutes = eval(input("Enter the minutes: "))
seconds = eval(input("Enter the seconds: "))


if (hours >=0 and hours <=23) and (minutes >=0 and minutes <=59) and (seconds >=0 and seconds <=59):
    print("Your time is valid")
else:
    print("Your time is invalid")

