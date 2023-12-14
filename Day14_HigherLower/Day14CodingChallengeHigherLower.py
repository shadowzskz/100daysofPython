#Coding Challenge: Higher lower game
#input: Choices
#output: High or low
import random

from art import *
from data import  data

def format(accont):
    account_name = accont["name"]
    account_desc = accont["description"]
    account_country = accont["country"]
    return (f"{account_name}, {account_desc} and {account_country}")

def check(guess, a_follow, b_follow):
    if (a_follow>b_follow):
        return guess == "a"
    else:
        return  guess == "b"

def gameplay():
    a = random.choice(data)
    b = random.choice(data)

    if a == b:
        b = random.choice(data)

    print(f"Compare A: {format(a)}")
    tprint("VS")
    print(f"Compare B: {format(b)}")

    choices = ['a', 'b']
    choice = input("Who has more followers A or B? ")
    while (choice.lower() not in choices):
        print("Enter either A or B: ")
        choice = input("Who has more followers A or B? ")

    a_followCount = a["follower_count"]
    b_followCount = b["follower_count"]
    is_correct = check(choice, a_followCount, b_followCount)
    return is_correct



def game():
    tprint("Higher or Lower")
    score = 0

    is_correct = gameplay()

    while (is_correct != False):
        score = score + 1
        print("You are right")
        print(f"Your score is {score}")
        is_correct = gameplay()

    else:
        print("Incorrect answer")
        print(f"Your score is {score}")

        choices = ['y', 'n']
        playrestart = input("Wish to Play again? Y or N: ")
        while (playrestart.lower() not in choices):
            print("Enter either Y or N: ")
            layrestart = input("Wish to Play again? Y or N: ")
        if playrestart.lower() == 'y':
            game()
        else:
            print("Thank you  for playing: ")


game()