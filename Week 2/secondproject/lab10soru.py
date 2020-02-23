print("Soru 2 :")

locations =['Istanbul','London','Amsterdam','Moskow','Berlin']

print("1)",locations)
print("2)",sorted(locations))
print("3)",locations)
print("4)",sorted(locations,reverse=True))
print("5)",locations)
locations.reverse()
print("6)",locations)
locations.reverse()
print("7)",locations)
locations.sort()
print("8)",locations)
locations.reverse()
print("9)",locations)

print("\nSoru 2 :")

language =[i for i in "Ptyhon Programming"]
print("1)",language)
language[0:len("Ptyhon")] = [i for i in "Python"]
print("2)",language)
language[len(language):] = [i for i in "Language"]
print("3)",language)
language.insert(6,"-")
print("4)",language)
language.sort()
print("5)",language)
language.reverse()
print("6)",language)
print("7)",language.count("a"))

print("\nSoru 3 :")

pizzaNames =['Pepperoni','Mushroom','Seafood','Mexican']
for names in pizzaNames:
    print(names)
print("---")

pizzaNames =['Pepperoni','Mushroom','Seafood','Mexican']
for names in pizzaNames:
    print("I like "+names + " pizza")
print("---")

pizzaNames =['Pepperoni','Mushroom','Seafood','Mexican']
for names in pizzaNames:
    print("I really like "+names + " pizza")
print("you can't make everyone happy because you're not a pizza.")

print("\nSoru 4 :")

liste = range(1,1000001)
print(min(liste))
print(max(liste))
print(sum(liste))

print("\nSoru 5 :")

numbers = list(range(1,20,2))
for number in numbers:
    print(number)

print("\nSoru 6 :")

q6 = list(range(3,33,3))
for numberq6 in q6:
    print(numberq6)

print("\nSoru 7 :")

another = list(i**3 for i in range(1,11))
for cube in another:
    print(cube)

print("\nSoru 8 :")

another = list(i**3 for i in range(1,11))
print(another)

print("\nSoru 9 :")

list = ['İstanbul', 34, 'Ahmet', 'Ankara', 6, False, 'İzmir']
print(list[0:3])
print(list[int (len(list)/2):int (len(list))-1])
print(list[-3:])


print("\nSoru 10 :")

t= ('rockfish sandwich','halibut nuggets','smoked salmon chowder','salmon burger','crab cakes')

print('You can choose from the following menu items:')
for i in t:
    print('-',i)
print('')
print('Our menu has been updated:')
print('You can choose from the following menu items:')
t= ('rockfish sandwich','halibut nuggets','smoked salmon chowder','black cod tips','king crab legs')
for i in t:
    print('-',i)