"""
Program: Guessing Game
Author:  Valliappan Ramanathan
Progam Description: Program To Guess the Secret Number
Revision: First Revision of the Guessing Game

"""
#Program Announcement
print("\n*** Program to guess The Secret Number ***\n")
#Importing Math Module
import math as m
#Importing Random Module
import random as r
#Getting the Range of maximum number from the user to choose a secret number
nMax = int(input("Enter the maximum number in the range: "))
#Using Ranrange assigning the secret number to variable s_no
s_no = (r.randrange(1,nMax))
#Getting the appropriate number of guesses to find the secret number
nGuess = int(m.log2(nMax)+1)
#Print the number range to guess the number
print(f"\nTry to guess the number from 1 to {nMax} (inclusive)\n")
#iterating the loop to guess the number within the number of guesses allowed
for i in range(1,nGuess,1):
    guess = int(input(f"You have {nGuess-i} {'Guess' if nGuess-i==1 else 'Guesses'} available \nEnter your Guess: "))
    if guess>s_no:
        print(f"the Secret number is less than {guess}.")
    elif guess<s_no:
        print(f"the Secret number is greater than {guess}.")
    elif guess==s_no:
        print("Congrats you found the secret number")
        break
else:
#Printing the output if all the available guesses are used
        print(f"You have no guess left \nThe secret number is {s_no}")
