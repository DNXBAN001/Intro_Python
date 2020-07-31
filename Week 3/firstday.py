# Name : Bandile Danxa
# Date : 19 May 2020
# Submission 7 - Firstday
# This program prints out the day on which the 1st of January falls can be


firstYear = eval(input("Enter the first year:\n")) #get the first year from user
secondYear = eval(input("Enter the second year:\n")) #get the second year from user

year = firstYear

#map R the reaminder of the formula with the actual day of the week
dayMap = {0: "Sunday", 1: "Monday", 2: "Tuesday",
          3: "Wednesday", 4: "Thursday", 5: "Friday",
          6: "Saturday"
          }

for i in range(secondYear-firstYear+1):
    day = 6 * ((year - 1) % 400)
    day = day + 4 * ((year - 1) % 100)
    day = day + 5 * ((year - 1) % 4) + 1
    day = day % 7
    print("The 1st of January ",year," falls on a ",dayMap[day])
    year +=1

