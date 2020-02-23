# CHAPTER 2 - CHAPTER 3
# Lists

motorcyles = ['honda', 'yamaha', 'suzuki']
print(motorcyles)

motorcyles[0] = 'ducati'
print(motorcyles)

motorcyles.append("kuga")
print(motorcyles)

cycles = []
cycles.append('honda')
cycles.append("yamaha")
print("Cycles :", cycles)

print('\n')
print("Eski hal :", motorcyles)
motorcyles.insert(0, 4)
print("Yeni hal :", motorcyles)
del motorcyles[4]
print('Silindikten sonra :', motorcyles)

popped_motorcyle = motorcyles.pop()
print("Pop element : ", popped_motorcyle)
print("Pop :", motorcyles)

first_owned = motorcyles.pop(0)
print("Pop(0) :", motorcyles)
motorcyles.append("renault")
motorcyles.append("ford")
motorcyles.append("nissan")
print("Yeni hal :", motorcyles)
motorcyles.remove('nissan')
print("Nissan silindi :", motorcyles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Cars", cars)
# cars.sort()
# print("Siralanmis hal :",cars)
# cars.sort(reverse = True)
# print("Ters sira :", cars)

print(sorted(cars))
print("Cars", cars)
print(len(cars))
print(cars.reverse())

motors = ['honda', 'yamaha', 'suzuki']
# print(motors[3]) error
print(motors[-1])

c =["Python","is","awesome"]
print(" ".join(c))

# Swap two number

a, b = 3, 4
print(a, b)
a, b = b, a
print(a, b)


