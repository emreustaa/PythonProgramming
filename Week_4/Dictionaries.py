aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if (alien['color'] == 'green'):
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
        print(alien)

favorite_languages = {'jen': ['python', 'ruby'],
                      'sarah': ['c'],
                      'edward': ['ruby', 'go']}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favourite languages are:")
    for language in languages:
        print("\t" + language.title())

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

for user, info in users.items():
    print("\nUsername: " + user)
    full_name = info['first'] + " " + info['last']
    location = info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

# isim = input("Please enter your name: ")
# print("Hello," + isim + "!")

# age = input("How old are you: ")
# print("My age : " + age)

# input

number = int(input("Enter a number, and I'll tell you if it's even or odd : "))
if (number % 2 == 0):
    print("The number ", number, "is even")
else:
    print("The number ", number, "is odd")

