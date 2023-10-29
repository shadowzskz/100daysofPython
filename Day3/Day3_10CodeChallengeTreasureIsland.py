#code Challenge
#Task: move left or right to win treasure
# input: Position left or right
# output: win or lose condition
print(''' _                                 _                       _
| |                               (_)                     (_)
| |__  _   _ _ __   __ _  ___  ___ _ _   _ _ __ ___  _ __  _ _ __   __ _
| '_ \| | | | '_ \ / _` |/ _ \/ _ \ | | | | '_ ` _ \| '_ \| | '_ \ / _` |
| |_) | |_| | | | | (_| |  __/  __/ | |_| | | | | | | |_) | | | | | (_| |
|_.__/ \__,_|_| |_|\__, |\___|\___| |\__,_|_| |_| |_| .__/|_|_| |_|\__, |
                    __/ |        _/ |               | |             __/ |
                   |___/        |__/                |_|            |___/ ''')
print("Welcome to Treasure Island\n Your mission is to find the treasure")
print("Your mission is to find the treasure")
pos: str = input("You are at a crossroad, where you want to go? Type \"left\" or \"right\"? ")
if (pos.lower() == "left"):
    print("you've comr to a lake. There is an island in the middle of the lake.")
    pos: str = input("Swim or wait? ")
    if (pos.lower() == "wait"):
        print("You have arrived a the island. There is a house with 3 doors")
        pos: str = input("Which door? Red, Blue or Yellow: ")
        if(pos.lower() == "yellow"):
            print("You fount the treasure. You won!")
        elif(pos.lower() == "red"):
            print("You have enter room full of lion, You are eaten alive. Game over")
        else:
            print("You have enter room of snakes you died. Game Over")
    else:
        print("You have drown. Game Over")
else:
    print("You fell into a hole. Game Over")
