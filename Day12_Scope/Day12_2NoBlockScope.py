#Block scope
gameLevel = 3
enemies = ["Skeleton","zombie","Alien"]

if gameLevel < 5:
    new_enemies = enemies[0]

print(f"No block scope within the if, while or for loop: {new_enemies}")

def noBlock():
    new_enemies = enemies[1]
    print(f"Scope inside function: {new_enemies}")


noBlock()