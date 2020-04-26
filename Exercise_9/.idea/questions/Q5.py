list_1 = [3, 5, 2, 4, 6]
list_2 = [4, 2, 4, 8, 13]

tupl = list(zip(list_1, list_2))

lastList = list(filter(lambda tup: (tup[1] % tup[0] != 0), tupl))
print(lastList)
