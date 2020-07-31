# Name : Bandile Danxa
# Date : 19 May 2020
# Submission 8 - Pi
#This program approximates the value of pi and use that value and radius read from user  to calculate the area of a circle

import math

pattern = 1
a = 1/2
term = (math.sqrt(2))/2
while term != 1:
    pattern = pattern * term
    term = term * a + a
    term = round(math.sqrt(term),3)

pi = round(2/pattern, 3) #approximate the pi variable
print("The approximation value of pi is : ",pi)

radius = eval(input("Enter the radius: ")) #read radius values from user
areaOfCircle = round((pi * (radius**2)), 3) #calculate area of circle and round the result to 3 decimals

print("Area: ", areaOfCircle) #print resulting area