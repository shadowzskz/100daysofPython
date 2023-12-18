from prettytable import PrettyTable

#Creating table object
table = PrettyTable()
table.add_column("Pokemon",["Pikachu", "Squirtle", "Charmander"])
table.align = "l"
table.add_column("Type",["Electric", "Water", "Fire"])
table.align = "r"
print(table)