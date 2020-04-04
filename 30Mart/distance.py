import math

# Euclidean Distance
def euclidean(x1, x2, y1, y2):
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

# Manhattan Distance
def manhattan(x1, x2, y1, y2):
    return abs((x1 - x2) + (y1 - y2))

# Supremum Distance
def supremum(x1, x2, y1, y2):
    return abs(max(x1, y1) - max(x2, y2))


 