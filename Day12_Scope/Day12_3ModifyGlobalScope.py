#Modify global Scope

enemies = "Skeleton"

def increase_enemies():
    global enemies ##Modify global scope
    ##Avoid modifying global scope
    enemies = "Zombie"
    print(f"Enemies inside function: {enemies}")

def withoutModifyingGlobal():
    return enemies + "1"

increase_enemies()
print(f"Enemies outside function: {enemies}")

print(withoutModifyingGlobal())