#CODING CHALLENGE
#TASK: Ceasar Cypher
#INPUT: input character
#OUTPUT: Encode the input

import pyfiglet

def EncodeChar(encodedInput, shiftlength):
    cipherText: str = ''
    for charval in encodedInput:
        asciiVal: int = int(ord(charval))
        asciiTochar: str = chr(asciiVal + shiftlength)
        cipherText = cipherText + asciiTochar
    return cipherText

def DecodeChar(decodedInput, shiftlength):
    plainText: str = ''
    for charval in decodedInput:
        asciiVal: int = int(ord(charval))
        asciiTochar: str = chr(asciiVal - shiftlength)
        plainText = plainText + asciiTochar
    return plainText

print(pyfiglet.figlet_format("caesar cipher"))
exitCase = ''
while(exitCase.lower()!='no'):
    action: str = input("Encode or Doecode:")
    if (action.lower() == 'encode'):
        encodedInput: str = input("Enter the character to encode: ")
        shiftlength: int = int(input("What shift length you want?: "))
        encodedData = EncodeChar(encodedInput, shiftlength)
        print(f"Your encoded msg is: {encodedData}")
        exitCase: str = input("Do you want to try again: Yes or No? ")

    elif (action.lower() == 'decode'):
        decodedInput: str = input("Enter the character to Decode: ")
        shiftlength: int = int(input("What shift length you want?: "))
        decodedData = DecodeChar(decodedInput, shiftlength)
        print(f"Your Decode msg is: {decodedData}")
        exitCase: str = input("Do you want to try again: Yes or No? ")
    else:
        print("You dont have a valid input")
        exitCase: str = input("Do you want to try again: Yes or No? ")
