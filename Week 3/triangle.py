# Name : Bandile Danxa
# Date : 18 May 2020
# Submission 3 - Triangle
#This program calculates the area of a triangle
import math

a = eval(input("Enter the length of the first side: "))
b = eval(input("Enter the length of the second side: "))
c = eval(input("Enter the length of the third side: "))

s = (a+b+c)/2
#area = (s*(s-a)*(s-b)*(s-c))**(0.5)
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("The area of the triangle with sides of length ",a," and",b," and",c," is",area)