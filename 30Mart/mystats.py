import math

# Calculate Mean of List
def mean(_list):
    return sum(_list) / len(_list)

# Calculate Standart Deviation of List
def stdev(_list):
    avg = mean(_list)
    return math.sqrt(sum(math.pow(item - avg, 2) for item in _list) / (len(_list) - 1))

# Find Mod of List
def mod(_list):
    frequencyList = {item: _list.count(item) for item in _list}
    return sorted(frequencyList, key=frequencyList.get, reverse=True)[0]

# Find Median of List
def median(_list):
    middle = int(len(_list) / 2)
    if len(_list) % 2 == 0:
        return (_list[middle] + _list[middle + 1]) / 2
    else:
        return _list[middle]