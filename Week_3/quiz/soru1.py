import random as rnd

rnd.seed(10)

print("Soru 1")

numbers = []
for i in range(20):
    numbers.append(int(1 + rnd.random() * 99))
for number in numbers:
    if number % 2 == 0:
        print(number, "is even number.")
    else:
        print(number, "is odd number.")

print("\nSoru 2")

age = 17
if age < 2:
    print("You're a baby.")
elif 2 <= age and age < 4:
    print("You're a toddler.")
elif 4 <= age and age < 13:
    print("You're a kid.")
elif 13 <= age and age < 20:
    print("You're a teenager!")
elif 20 <= age and age < 65:
    print("You're a teenager!")
elif 65 <= age:
    print("You're an elder")

print("\nSoru 3")

current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

newList = [x.lower() for x in current_users]

for users in new_users:
    if users.lower() not in newList:
        print("Great, " + users + " is still available.")
    else:
        print("Sorry " + users + ", that name is taken.")

print("\nSoru 4")

print("")
dictionary = {'first_name ': 'eric', 'last_name': 'matthes', 'age': 43, 'city': 'sitka'}

for info in dictionary.values():
    print(info)

print("\nSoru 5")

print("")

favorite_numbers = {
    'mandy': 42,
    'micah': 23,
    'gus': 7,
    'hank': 1000000,
    'maggie': 0,
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {numbers}.")

print("\nSoru 6")

print("")

rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("")
print("The following rivers are included in this data set:")
for countries in rivers.keys():
    print("- " + countries.title())

print("")
print("The following countries are included in this data set:")
for countries in rivers.values():
    print("- " + countries.title())

print("\nSoru 7")

print("")

persons = [{'first_name': 'eric', 'last_name': 'matthes', 'age': 43, 'city': 'sitka'},
           {'first_name': 'ever', 'last_name': 'matthes', 'age': 5, 'city': 'sitka'}, ]

for peoples in persons:
    print(f"{peoples['first_name']} {peoples['last_name']}, of {peoples['city']}, is {peoples['age']} years old.")

print("\nSoru 8")

print("")

database = [('John Reese', 'Computer'), ('Harold Finch', 'Mobile Phone'), ('Carl Elias', 'Knife'),
            ('John Reese', 'Mouse'), ('Harold Finch', 'Phone Case'), ('Carl Elias', 'Tomato'),
            ('John Reese', 'Keyboard'), ('Harold Finch', 'Router'), ('Carl Elias', 'Chess')]


def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di


dictionary = {}
Convert(database, dictionary)

for key, value in sorted(dictionary.items()):
    print(f"{key} : {value}")
