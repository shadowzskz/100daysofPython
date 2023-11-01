#CodingChallenge
#Task: add travel longs
#input: DIctionary
#Output: sAdd an new country visited

def countryVisits(travel_log):
    for data in travel_log:
        print(data)

def addNew():
    emmptyDict = {}
    countryVisited: str = input("Enter the name of visited countries: ")
    emmptyDict['country'] = countryVisited
    visits: int = int(input("Enter the num of visits: "))
    emmptyDict['visits'] = visits
    numVisited: int = int(input("How many places you visited: "))
    listPlaces = []
    for places in range(numVisited):
        lisPlace: str = input("Enter the city name: ")
        listPlaces.append(lisPlace)
    emmptyDict['cities'] = listPlaces

    travel_log.append(emmptyDict)

travel_log = [
    {
        'country': 'France',
        'visits': 12,
        'cities': ['Paris', 'Lille', 'Dijon'],
    },
    {
        'country': 'Germany',
        'visits': 5,
        'cities': ['Berlin', 'Hamburg', 'Stuttgart'],
    },

]
print(f"Your travel logs: ")
countryVisits(travel_log)
print("Add new travel Data")
addNew()



print("Your update country list: ")
countryVisits(travel_log)