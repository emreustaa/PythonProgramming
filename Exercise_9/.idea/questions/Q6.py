numbers = [153, 371, 372, 1634]


def splitNumber(number):
    return [int(i) for i in str(number)]

print(list(filter(lambda num : sum([pow(x,len(splitNumber(num))) for x in splitNumber(num)])==num,numbers)))