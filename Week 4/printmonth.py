# Name : Bandile Danxa
# Date : 25 May 2020
# Submission 4 - Printmonth
# This program prints out the number of days in a month according to their respective days (in a grid format)

#function for checking whether the entered month is valid or not
def isMonthValid(month):
    monthList = ["january", "february", "march", "april", "may", "june",
                 "july", "august", "september", "october", "november", "december"]
    for i in monthList:
        if month == i:
            return True
    return False

#function for verifying whether the entered start day is valid or not
def isStartDayValid(startDay):
    dayList = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    for j in dayList:
        if startDay == j:
            return True
    return False


month = input("Enter the month('January', ...,'December'): \n").lower() #get month and store value on month variable, convert to lowercase
startDay = input("Enter the start day ('Monday', ..., 'Sunday'): \n").lower() #get start day and store value on startDay variable

numberOfDays = {"january": 31, "february": 28, "march": 31, "april":30, "may": 31, "june": 30, "july": 31,
                "august": 31, "september": 30, "october": 31, "november": 30, "december": 31}
daysDictionary = {"monday": 7, "tuesday": 6, "wednesday":5, "thursday":4, "friday":3, "saturday":2, "sunday":1}

days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
daysMap = {"monday":"Mo", "tuesday":"Tu", "wednesday":"We", "thursday":"Th", "friday":"Fr", "saturday":"Sa", "sunday":"Su"}

dayNumber = 1
startPosition = 0 #variable to store the position in which we start printing the starting day

#check whether the month and starting day entered are valid, if true then proceed
if isMonthValid(month) and isStartDayValid(startDay):

    # print the days' headings in horizontal format
    for day in days:
        print(day, end=" ")

    print() #go to newline

    #as long as the day entered doesnt match the day in days' list, peform some justification to the right
    #by leaving free spaces, when done break out of the loop
    for q in days:
        startPosition += 2
        if q != daysMap[startDay]:
            startPosition += 1
        else:
            dayNumber = str(dayNumber).rjust(startPosition) #right justify with a field width of startPosition value
            break

    #start printing out the days' number of the first row, with correct justification and spaces in between each number
    for i in range(daysDictionary[startDay]):
        #make spaces in between numbers as long as it not the last in the row
        if i < daysDictionary[startDay]-1:
            print(dayNumber, end=" ")
        #if it is last then do not make space at the end
        else:
            print(dayNumber, end="")
        dayNumber = str(int(dayNumber) + 1) #update dayNumber
        dayNumber = dayNumber.rjust(2) #right justify with a field width of 2

    print() #go to newline
    dayNumber = daysDictionary[startDay]+1 #update the value of dayNumber

    #print out the remaining days' numbers in the column and row format
    for j in range(6):
        for k in range(7):
            dayNumber = str(dayNumber).rjust(2) ##right justify with a field width of 2
            # make spaces in between numbers as long as it not the last in the row
            if k < 6:
                print(dayNumber, end=" ")
            # if it is last then do not make space at the end
            else:
                print(dayNumber, end="")
            dayNumber = int(dayNumber)+1 #update the value of dayNumber

            #break out of the inner loop if the day number is greater than number of days in the particular month
            if int(dayNumber) > numberOfDays[month]:
                break
        # break out of the outer loop if the day number is greater than number of days in the particular month
        if int(dayNumber) > numberOfDays[month]:
            break
        print() #go to new line

#else if the month and/or the start day entered are not valid then print a warning message on the
else:
    print("Month and/or start day entered is not valid")