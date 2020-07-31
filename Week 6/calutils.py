# Name : Bandile Danxa
# Date : 08 June 2020
# Submission 1 - Calcutils



monthDictionary = { 1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
                        7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
monthMap = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June":6,
                    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
dayMap = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
numberOfDaysInAMonth = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31,
                    "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}

#This function checks whether the year passed is a leap or not, return true if it is leap
def isLeapYear(year):
    if ((year % 4== 0) and (year % 100 != 0)) or (year%400==0):
        return True
    return False

#This function takes the month number and returns the month name corresponding to the number
def monthName(monthNumber):
    # traverse through the dictionary and check if the value of the number entered matches any value in the dictionary
    for month in monthDictionary:
        # if match is found the return the value of the match
        if monthDictionary[month] == monthDictionary[monthNumber]:
            return monthDictionary[month]
    return "The number entered does not correspond to any month in the dictionary"

#This function takes the year and month number and returns the number of days fot that particular month
def daysInMonth(monthNumber, year):
    if isLeapYear(year):
        #if the year is leap and the month is february, then add an extra 1 day
        if monthName(monthNumber) == "February":
            return numberOfDaysInAMonth[monthName(monthNumber)]+1

    return numberOfDaysInAMonth[monthName(monthNumber)]

def firstDayOfYear(year):
    day = 6 * ((year - 1) % 400)
    day = day + 4 * ((year - 1) % 100)
    day = day + 5 * ((year - 1) % 4) + 1
    day = day % 7
    return day

def firstDayOfMonth(monthNumber, year):
    firstDay = firstDayOfYear(year)
    y = 1
    for i in range(monthNumber+1):
        if y == 1:
            print()
        elif y <= monthNumber:
            x = daysInMonth(y - 1, year) - 28
            firstDay += x
            if firstDay >= 7:
                firstDay = firstDay % 7
        y += 1

    return firstDay


option = ""

while option != 0:
    print("Choose from the following options: \n")
    print("0. Quit/Exit.\n"
          "1. Test isLeapYear().\n"
          "2. Test monthName().\n"
          "3. Test daysInMonth().\n"
          "4. Test firstDayOfYear().\n"
          "5. Test firstDayOfMonth().\n")
    option = int(input())
    if option == 1:
        year = int(input("Enter the year (4 digits):\n"))
        if isLeapYear(year):
            print("The year",year,"is a leap year")
        else:
            print("The year",year,"is not a leap year")
    
    elif option == 2:
        for i in monthDictionary:
            print("Month number",i,"is",monthDictionary[i])
    elif option == 3:
        monthNumber = int(input("Enter month number:\n"))
        print("The number of days in month number",monthNumber,"is",numberOfDaysInAMonth[monthDictionary[monthNumber]])
    elif option == 4:
        year = int(input("Enter the year (4 digits);\n"))
        print("The first day of the year",year,"is day number",firstDayOfYear(year),"("+dayMap[firstDayOfYear(year)]+")")
    elif option == 5:
        year = int(input("Enter the year (4 digits);\n"))
        monthNumber = int(input("Enter a month number;\n"))
        print("The first day of",monthDictionary[monthNumber],"of",year,"is day number",
              firstDayOfMonth(monthNumber, year),"("+dayMap[firstDayOfMonth(monthNumber, year)]+")")




print("Application exited")

# year = 2020
# print(isLeapYear(year))
# print(monthName(6))
# print("The number of days in the month is : ", daysInMonth(2, year))
# print("The 1st of January of ", year, "falls on day ", firstDayOfYear(year))
# print("The first day of ", monthName(5)," is on day", firstDayOfMonth(5, year))
