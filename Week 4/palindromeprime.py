# Name : Bandile Danxa
# Date : 27 May 2020
# Submission 4 - PalindromePrime
# This program finds all palindromic primes between two integers supplied as input (start and end points are excluded).


def isPrime(number):
    divisor = 2
    if number < divisor:
        return False
    if number == divisor:
        return True
    while divisor < number:
        if (number % divisor)==0:
            return False
        divisor +=1
    return True

def isPalindrome(text):
    reversedText = ""
    txt = str(text)
    x = -1
    for i in range(len(txt)):
        reversedText += txt[x]
        x -= 1
    if txt == reversedText:
        return True
    return False

N = int(input("Enter the start point N: \n"))
M = int(input("Enter the end point M: \n"))
foundAny = False
print("The palindromic primes are : ")
for n in range(M):
    if isPrime(n) and isPalindrome(n):
        if n > N:
            print(n)
            foundAny = True

if not (foundAny):
    print("No palindrome primes have been found in the range specified")
