import random
import pyfiglet
from typing import List


def displayIntro():
    print(pyfiglet.figlet_format("Welcome to Guessing Game"))
    choicePlay()


def choicePlay():
    level_guess: List[str] = ['easy', 'hard']
    choice: str = input("Enter the level of your choice 'easy' or 'hard': ")
    while choice.lower() not in level_guess:
        print("Incorrect Guess: ")
        choice = input("Enter the level of your choice 'easy' or 'hard': ")
    if choice.lower() in level_guess:
        print("Guess the number between 1 and 100 ")
        if choice.lower() == 'easy':
            print("You have 10 guesses left: ")
            gameplay(choice)
        else:
            print("You have 5 guesses left: ")
            gameplay(choice)


def gameplay(choice):
    num: int = random.randint(1, 100)
    if choice == 'easy':
        count = 10
    else:
        count = 5

    while count != 0:
        guess = int(input("Make a guess: "))

        if guess == num:
            print("You are correct! You won")
            break
        elif guess > num:
            print("HIGH")
            if ((guess -num)>20):
                print("Your guess is too high")
            elif ((guess -num)>10 and (guess-num)<20):
                print("Your guess is slighly  high")
            else:
                print("You are near")

        else:
            print("LOW")
            if ((num -guess)>20):
                print("Your guess is too high")
            elif ((num -guess)>10 and (num -guess)<20):
                print("Your guess is slighly  high")
            else:
                print("You are near")

        count -= 1

    if count == 0:
        print("You run out of guesses: ")
        print(f"Correct num is: {num}")
        print(pyfiglet.figlet_format("You lose"))
        playAgain()


def playAgain():
    play = input("Play again Y or N? ")
    play_guess: List[str] = ['y', 'n']
    while play.lower() not in play_guess:
        print("Incorrect Guess: ")
        play = input("Play again Y or N? ")

    if play.lower() in play_guess:
        if play.lower() == 'y':
            choicePlay()
        else:
            print(pyfiglet.figlet_format("Thank you for playing"))


def main():
    displayIntro()


if __name__ == '__main__':
    main()
