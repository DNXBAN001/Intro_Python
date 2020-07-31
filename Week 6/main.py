# Bandile Danxa
# Date 08 June 2020
# Week 6


# Submission 1 : Calutils.py
import calutils

# test program for Bukiyip calculations
import bukiyip
print('**** Bukiyip test program ****')
print('Available commands:')
print('d <number> : convert given decimal number to base-3.')
print('b <number> : convert given base-3 number to decimal.')
print('a <number> <number> : add the given base-3 numbers.')
print('m <number> <number> : multiply the given base-3 numbers.')
print('q : quit')
print()
while True:
    choice = input ("Enter a command:\n")
    action = choice[:1]
    if action == 'q':
        break
    elif action == 'b' or action == 'd':
        num = int(choice[2:])
        if action == 'b':
            print(bukiyip.bukiyip_to_decimal (num))
        else:
            print(bukiyip.decimal_to_bukiyip(num))
    elif action == 'a' or action == 'm':
        num1, num2 = map (int, choice[2:].split(" "))
        if action == 'a':
            print(bukiyip.bukiyip_add (num1, num2))
        else:
            print(bukiyip.bukiyip_multiply (num1, num2))


# test program for english/piglatin translator
import piglatin

choice = input ("(E)nglish or (P)ig Latin?\n")
action = choice[:1]
if action == 'E':
    s = input("Enter an English sentence:\n")
    new_s = piglatin.to_pig_latin(s)
    print("Pig-Latin:")
    print(new_s)
elif action =='P':
    s = input("Enter a Pig Latin sentence:\n")
    new_s = piglatin.to_english(s)
    print("English:")
    print(new_s)