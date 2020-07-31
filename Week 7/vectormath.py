# Submission 4
# Date : 15 June 2020

import math

#This function perfomrs the addition of two vectors
def addition(vec1, vec2):
    sum = []
    for i in range(len(vec1)):
        sum.append(vec1[i]+vec2[i])
    return sum

#This function performs dot product of two vectors
def dotProduct(vec1, vec2):
    summedElements = addition(vec1, vec2) #use the addition function to perform sum
    dotProduct = 0
    #from here we have the list of summed elements and we only need to add all the elements in the summedElements list and our dot product is done
    for i in summedElements:
        dotProduct += i # go through each element in the summedElements list and add it on the dotPoduct variable
    return dotProduct

# This function gives the normalization of a single vector
def nomarlization(vector):
    norm = 0
    sum = 0
    for i in vector:
        sum += i**2
    norm = round(math.sqrt(sum), 2)
    return norm


def main():
    print("Enter vector A:\n")
    A = list(map(int, input().split()))
    print("Enter vector B:\n")
    B = list(map(int, input().split()))

    print("A+B = ", addition(A, B))
    print("A.B = ", dotProduct(A, B))
    print("|A| = ", nomarlization(A))
    print("|B| = ", nomarlization(B))

main()