#code Challenge
#task: While pay the bill around bill, everyone put out their card and whosever card is pick out needs to pay
#input: Name of friends
#output: pick out random friend
from typing import List
import random

print("COding Challlenge Bank Roulette")
numberFriends:int = int(input("How many friends are there: "))
friends: List[str]= []
for friend in range(0,numberFriends):
    name:str = input("Input your friends name: ")
    friends.append(name)
print(f"Here are your friends list: {friends}")
print(f"{friends[random.randint(0,numberFriends-1)]} will pay the bill today")