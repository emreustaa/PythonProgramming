# CHAPTER 4

# Working more with Lists

names = ["ali", "ahmed", "bob"]
for name in names:
    print(name)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ', that was a agreat trick')
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show")

for magic in magicians:
    print(magic.title() + ", that was a great trick!")
print("I can't wait to see your next trick," + magic.title() + ".\n")

for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

newList = list(range(1, 1001))
print(newList)

even_numbers = list(range(8, 100, 8))
print(even_numbers)


print("\nFirst 10 square :")

deger = []

for square in range(1, 11):
    deger.append(pow(square, 2))
print(deger)

print("\nFirst 10 square  alternatif:")

another = list(i*i for i in range(1,11))
print(another)


players = ['charles','martina','michael','floroence','eli']
print(players[0:3])
#["charles","martina","michael"]
print(players[1:4])

print("--------")
print(players[:4]) # soldan ilk 4 u
print(players[3:]) # soldan kac tane yazilmicak
print(players[-3:]) # sagdan ilk 3 u yaz

print("\nCopying a list : ")
my_foods = ['pizza','falafel','carror cake']
friends_food= my_foods
my_foods.append("cannolo")
friends_food.append('ice cream')
print("\nMy favourite foods are : ")
print(my_foods)
print("\nMy friends favorute foods are : ")

print(friends_food)
print("--------")

friends_food = my_foods[:] # if we want copy, we must use this two dots
print(friends_food)


#Tuples
print("\n")
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
dimensions =(250,100)
print(dimensions[0])
print(dimensions[1])