#List: Data structure
from typing import List

print("List starts with index 0")
fruit: List[str] = ['apples', 'banana', 'orange']
print(fruit)
print(f"fruit[0]: {fruit[0]}, fruit[1]: {fruit[1]}, fruit[2]: {fruit[2]}")
print("List can be reversed using negative index")
print(f"fruit[-3]: {fruit[-3]}, fruit[-2]: {fruit[-2]}, fruit[-1]: {fruit[-1]}")
print("List are immultable")
fruit[2]='grapes'
print(f"fruit[2]=\"grapes\"{fruit[2]}")
print(fruit)
print("List can be appeded using apped method")
fruit.append("orange")
print(f"fruit.append(\"orange\"): {fruit}")
print("List cab be extended with  additional list")
fruit.extend(["Melons", "Guava"])
print(f"fruit.extend([\"Melons", f"Guava\"]): {fruit}")
print("There are multple methods on list such as insert, remove, pop")
fruit.insert(2, "coconut")
print(f"fruit.insert(2, \"coconut\") insert(position, ListItem): {fruit}")
fruit.remove(2)
print(f"fruit.remove(2) remove(position): {fruit}")
fruit.pop([4])
print(f"fruit.pop([f]) pop([position]): {fruit}")
fruit.clear();
print(f"fruit.clear() remove list: {fruit}")
print("Index out of range error exist if arrya is requsted beyond the limits")