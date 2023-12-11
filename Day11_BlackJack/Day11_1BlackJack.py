#CODING CHALLENGE
#TASK: BlackJack
#INPUT: add more cards?
#OUTPUT: Win or lose
import random
import pyfiglet
from typing import List

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)


def displayIntro():
    print(pyfiglet.figlet_format("Welcome to BackJack Game"))
    choicePlay()

def displayCard(turn, num, symbol, hide=True):
    rows = ['', '', '']
    print(turn)
    if turn == 'dealer' and hide==False :
        rows[0] += '|## | '
        rows[1] += '|###| '
        rows[2] += '|_##| '
    else:
        rows[0] += '|{} | '.format(num.ljust(2))
        rows[1] += '| {} | '.format(symbol)
        rows[2] += '| {}| '.format(num.rjust(2, ' '))
    for row in rows:
        print(row)

def exitGamePlay():
    print(pyfiglet.figlet_format("Thankyou for playing the game"))

def cardPlay():
    symbols = [HEARTS, DIAMONDS, SPADES, CLUBS];
    num: List[str] = str(random.randint(1, 13))
    symbolChoice:int = random.randint(0,3)
    symbol = symbols[symbolChoice]
    return num,symbol


def choicePlay():
    choice:List[str] = ['y', 'n']
    userInput:str = ''
    userInput: str = input("Do you want to play? Y or N: ")
    while(userInput not in choice):
        print(f"Invalid character f{userInput}, press either Y or N")
        userInput: str = input("Do you want to play? Y or N: ")
    if (userInput.lower()=='y'):
        gameplay()
    else:
        exitGamePlay()

def getCard():
    choice: List[str] = ['y', 'n']
    userInput: str = ''
    userInput: str = input("Do you want to get card? Y or N: ")
    while (userInput not in choice):
        print(f"Invalid character f{userInput}, press either Y or N")
        userInput: str = input("Do you want to get card? Y or N: ")
    return userInput

def gameplay():
    hide=True
    turn:dict = {
            'dealer': {
                'count': 0,
                'cards': [],
                'symbol': [],
                'modifiedCards': [],
                'sum': 0
            },
            'player': {
                'count': 0,
                'cards': [],
                'symbol': [],
                'modifiedCards': [],
                'sum': 0,
            },
        }
    count = 1
    for play in range(3):
        print(f"Play {play+1}")
        for role in turn:
            print(f"Role {role}")
            playcount = cardPlay()
            num, symbol = playcount
            turn[role]['cards'].append(num)
            turn[role]['symbol'].append(symbol)
            turn[role]['count'] += 1
            #print(list(turn.keys())[roleValue])
            if(play>0):
                hide=False
            displayCard(role, num, symbol,hide)

        a = modify_card_value(turn[role]['cards'][play],role,turn[role]['sum'])
        turn[role]['modifiedCards'].append(a)
        turn[role]['sum'] = sum((turn[role]['modifiedCards']))

        count = count + 1
        if(turn[role]['count']<=2):
            getData = getCard().lower()
            if(getData=='y'):
                player_cards_sum =  turn['player']['sum']
                if (player_cards_sum > 21):
                    print("You lose")
                    break
                continue
            elif (getData=='n'):
                print("Dealer cards are: ")
                for num in range(0, count-1):
                    displayCard('dealer',turn['dealer']['cards'][num],turn['dealer']['symbol'][num])
                    a = modify_card_value(turn['dealer']['cards'][num],turn['dealer'],turn['dealer']['sum'])
                    turn['dealer']['modifiedCards'].append(a)
                    turn['dealer']['sum'] = sum(turn['dealer']['modifiedCards'])
                dealerSum = turn['dealer']['sum']
                print('Dealer sum:', dealerSum)
                # print(dealerCount)
                print("Player cards are: ")
                for num in range(0, count-1):
                    displayCard('Player', turn['player']['cards'][num], turn['player']['symbol'][num])
                playerSum  = turn['player']['sum']
                print('Player sum:', playerSum)
                if (dealerSum <= 21 and playerSum <= 21):
                    if (dealerSum > playerSum):
                        print(pyfiglet.figlet_format("You lose"))
                    else:
                        print(pyfiglet.figlet_format("You Won"))
                elif (dealerSum > 21 and playerSum <= 21):
                    print(pyfiglet.figlet_format("You Won"))
                else:
                    print(pyfiglet.figlet_format("You Lose"))
                break
        else:
            print("Dealer cards are: ")
            for num in range(0, count - 1):
                displayCard('dealer', turn['dealer']['cards'][num], turn['dealer']['symbol'][num])
                a = modify_card_value(turn['dealer']['cards'][num], turn['dealer'], turn['dealer']['sum'])
                turn['dealer']['modifiedCards'].append(a)
                turn['dealer']['sum'] = sum(turn['dealer']['modifiedCards'])
            dealerSum = turn['dealer']['sum']
            print('Dealer sum:', dealerSum)
            # print(dealerCount)
            print("Player cards are: ")
            for num in range(0, count - 1):
                displayCard('Player', turn['player']['cards'][num], turn['player']['symbol'][num])
            playerSum = turn['player']['sum']
            print('Player sum:', playerSum)
            if (dealerSum <= 21 and playerSum <=21):
                if (dealerSum > playerSum):
                    print(pyfiglet.figlet_format("You lose"))
                else:
                    print(pyfiglet.figlet_format("You Won"))
            elif (dealerSum > 21 and playerSum <=21):
                print(pyfiglet.figlet_format("You Won"))
            else:
                print(pyfiglet.figlet_format("You Lose"))
            break


def modify_card_value(card, role, sum=0):
    if (role=='player'):
        if card == "1":
            user_input = int(input(f"Do you want to treat '1' as 1 or 11 for card {card}? Enter 1 or 11: "))
            if user_input == 1:
                return 1
            elif user_input == 11:
                return 11
            else:
                raise ValueError("Invalid input. Please enter either 1 or 11.")
        if card in ["11", "12", "13"]:
            return 10
        else:
            return int(card)
    elif (role=='dealer'):
        if (sum <=10):
            return 11
        else:
            return 1

    else:
        if card in ["11", "12", "13"]:
            return 10
        else:
            return int(card)

def main():
    # displayIntro()
    gameplay()



if __name__ == '__main__':
    main()
