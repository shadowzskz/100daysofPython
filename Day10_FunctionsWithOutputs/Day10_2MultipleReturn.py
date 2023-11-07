def formatedName(fName, lName):
    if (fName=="" or lName==""):
        return "You didnt provided valid inputs"
    formattedFname = fName.title()
    formattedLname = lName.title()
    return f"{formattedFname} {formattedLname}"


print(formatedName("", ""))
print(formatedName("SAHAJ", "SHAKYA"))