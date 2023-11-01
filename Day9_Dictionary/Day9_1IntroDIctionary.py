#Dictionary
# Syntax
# dictionaryWord= {'key': 'val'}
# dictVal[key]
print("DIctionary seperates key value pairs")
dictVal = {
    '1': 'You are god',
    '2': 'You are devil',
    '3': 'You are human',
}

print(dictVal)
print("Fetch dictionay")
print(f"dictVal['1']: {dictVal['1']}")
print(f"dictVal['2']: {dictVal['2']}")
print(f"dictVal['3']: {dictVal['3']}")
print("Edit a Dictionary")
dictVal['1']="I am god"
print(f"dictVal['1']=\"I am god\": {dictVal['1']}")
print("Looping through dictionay just gives keys")
for val in dictVal:
    print(val)
print("passing key to dictionay throug loops gives value ie loop[key]")
for val in dictVal:
    print(dictVal[val])
print("Printing key and value")
for val in dictVal:
    print(val, dictVal[val])