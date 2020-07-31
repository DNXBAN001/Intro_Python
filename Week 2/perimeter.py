#Name : Bandile Danxa
#Date 13 May 2020
#submission 10
#Program for calculatiing perimeter of the required fence and the its associated total cost

w1 = eval(input("Enter width 1: "))
h1 = eval(input("Enter height 1: "))
w2 = eval(input("Enter width 2: "))
h2 = eval(input("Enter height 2: "))
pricePerMetre = eval(input("Enter price per metre : "))

fenceRequired = 2*(w1+w2)+h1+h2+(h1-h2)      #calculate perimeter (total fence required)
totalPrice = pricePerMetre*fenceRequired      #calculate total price of the required fence

print("The total fence required = ", fenceRequired)
print("The total price = ", totalPrice)