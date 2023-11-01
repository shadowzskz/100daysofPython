#ONLY DICT
# {
#     key1: val1,
#     key2: val2,
# }
# Nested list to dict
# {
#     key1: List],
#     key2: val2,
# }
# Nesting list and dict
# {
#     key: [List],
#     key2: {Dict}
# }

print("Sample Dictionay only")
capitals = {
    'Nepal': 'Kathmandu',
    'India': 'Delhi',
}
lsting = ['Asia', 'Europe']
print(capitals)
print("Sample Dictionay nested with list")
nested = {
    'continents': lsting,
    'Planet': 'Earth'
}
print(nested)
nestedDicList = {
    'continent': lsting,
    'countries': capitals
}
print("Sample Dictionay nested with list and Dictionary")
print(nestedDicList)
nextLevelNestng = {
    'France': {"citiesVIsited": ["Paris","Dijon"]},
    'Germany': ["Berlin", "Hamburg"]
}
print("Sample Dictionay nested with list and Dictionary 2")
print(nextLevelNestng)
apidata = [capitals, nestedDicList, nextLevelNestng]
print("How apu datas are obtained")
print(apidata)