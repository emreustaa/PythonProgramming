# JUPYTER EXAMPLES

cities = ['Istanbul', 'Izmir', 'Ankara']
print(cities)

characterList = list('Python Language')
print(characterList)

languages = ['Python', 'Java', 'C', 'C++']
languages.append("R")
print(languages)

languages.append(["Rust", "Dart"])
print(languages)

languages[len(languages):] = ['PHP', 'Javascript']
print(languages)

brands = ['Hyundai', 'Fiat']
brands.insert(0, 'Ford')
print(brands)

brands.insert(1, ['Lexus', 'Nissan'])
print(brands)

L1 = ['A', 'B', 14]
L2 = ['C', 'D', 23]
print(L1 + L2)

print(L1 * 3)

index = L1.index("B")
print(index)

C = [10, 80, 1, 45, 0]
C.sort()
print(C)

C = [10, 80, 1, 45, 0]
print(sorted(C))
print(C)

C.reverse()
print(C)

# Temmizle

# C.clear()
# print(C)

# For loop

mixList = ['Istanbul', 34, 'Izmir', 35, 'Ankara', 6]
for item in mixList:
    print(item)

number_list = list(range(100, 1, -1))
print(number_list)


print("\n")
print("Min:" , min(number_list))
print("Max:" , max(number_list))
print("Sum:" , sum(number_list))

# 1 den 10 a kadar olan elemanlarin karesi

L =[i**2 for i in range(1,11)]
print(L)


print(number_list[0:5])

print("\nIkiser ikiser")
print(number_list[::2])
print("\nTersten yaz")
print(number_list[::-1])
