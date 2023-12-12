#NameScope and Global Scope

#Scope => A variable is only available from inside the region it is created

enemies = 1

def increase_enemies():
   enemies = 2
   print(f"Enemies inside local scope: {enemies}")

increase_enemies()
print(f"Enemies on global scope: {enemies}")