# if statement and dictionaries

cars = ['audi', 'bmw', 'subaru']

carList = [car for car in cars]
print(carList)

number = list(range(3, 10))
print(number)

car = 'Audi'

print(car.lower() == 'audi')
print(car == 'audi')

answer = 42
if answer != 42:
    print("True")
else:
    print("False")

banned_users = ['andrew', 'carolina']
user = 'andrew'

if user not in banned_users:
    print(user.title() + ",you can post a respobse if you wish.")
else:
    print(user.title() + " in list.")

age = 12;
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

age = 12;
if age < 4:
    odul = 0
elif age < 18:
    odul = 5
else:
    odul = 10

print("Your admission cost is $" + str(odul) + ".")
print("")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_toppings in requested_toppings:
    print("Adding " + requested_toppings + ".")

print("\nFinished making your pizza!")

myList = ["red", "yellow", "green"]
if len(myList) == 0:
    print("The list is empty!")
else:
    print("The list is not empty")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0.get('color'))
print(alien_0.get('points'))
print(alien_0)
alien_0['x_position'] = 0

alien_0['y_position'] = 25
print(alien_0)
print(alien_0.get('x_position'))
print(alien_0.get('y_position'))
del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',

}
print(favorite_languages['jen'])

print({x: x ** 2 for x in (2, 4, 6)})

user_0 = {
    'username': 'emreustaa',
    'first': 'emre',
    'last': 'usta',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

print("")
friends = ['phil', 'sarah']
for name in sorted(favorite_languages.keys()):
    print(name.title())

    if name in friends:
        print("Hi " + name.title() + ", I see you favourite languages is " + favorite_languages[name].title() + "!")

print("")
for languages in set(favorite_languages.values()):
    print(languages.title())

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print("")
print(dict.items())
dict.clear()
print(dict.items())
print("")

sozluk ={'Isim' :'Emre','Soyisim' : 'Usta'}
print(sozluk.items())
del sozluk
print(sozluk.items())

